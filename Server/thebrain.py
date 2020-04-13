# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import socket
import os
import cv2
import speech_recognition as sr


###################################################################################################
def qrcode(): 
    
    image = cv2.imread('image.jpg')     
    qrCodeDetector = cv2.QRCodeDetector()     
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)     
    if points is not None:     
        nrOfPoints = len(points)     
        for i in range(nrOfPoints):
            nextPointIndex = (i+1) % nrOfPoints
            cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)     
        return decodedText     

    else:
        return 0     

###################################################################################################

###################################################################################################
def speech_to_text():
    

    r = sr.Recognizer()
    audio = sr.AudioFile('audio.wav')
    with audio as source:
        r.adjust_for_ambient_noise(source,duration=0.1)
        audio = r.record(source)
    try:
        message = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        message = "silence"
    except sr.RequestError as e:
        print("Could not understand audio")
        message = "silence"
    return  message
    

    
###################################################################################################        
        
        
        
        
HOST = '192.168.1.14'  # Standard loopback interface address (localhost)
PORT = 10001        # Port to listen on (non-privileged ports are > 1023)
camera,audio,case,info= 0,0,0,0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            if data == b'Ready':
                conn.sendall(b"BeginLearning.endmes")
                audio=1


            elif data == b'Learning done':
                conn.sendall(b"SendMeInfo.endmes")
                audio=0
                info=1                
                
                
                
            else:
                ##############################################################
                if audio == 1:
                    length=int(data)
                    conn.sendall(b"ContinueWithVoice.endmes")                    
                    audio = 2
                elif audio == 2:
                    t = open("audio.wav", "ab+")
                    t.write(data)
                    t.close()
                    bytes = os.stat('audio.wav').st_size
                    if bytes == length:
                        audio = 1
                        message=speech_to_text()
                        os.remove("audio.wav")
                        mystring= "BeginLearning.endmes" + "first"
                        string = mystring.encode('utf-8')
                        conn.sendall(string)
                ##############################################################                      
                        
                elif camera == 1:
                    length=int(data)
                    conn.sendall(b"ContinueWithCamera.endmes")                    
                    camera = 2         
                elif camera == 2:
                    t = open("image.jpg", "ab+")
                    t.write(data)
                    t.close()
                    bytes = os.stat('image.jpg').st_size

                    if bytes == length:
                        camera = 0                   
                        text=qrcode()
                        os.remove("image.jpg")
                        conn.sendall(b"Hands.endmes")
                ##############################################################
                elif info ==1:
                    data=data.decode('utf-8')
                    sumpas = int(data.split('.')[0])  
                    sumlaw = int(data.split('.')[1])
                    sumsaving = int(data.split('.')[2])
                    sumswerve = int(data.split('.')[3])
                    if (sumpas == sumlaw) or (sumpas == sumsaving) or (sumsaving == sumlaw) or (sumswerve == sumlaw) or (sumswerve == sumsaving) or (sumswerve == sumpas):
                        print(sumpas)
                        print(sumlaw)
                        print(sumsaving)
                        print(sumswerve)
                    info =0
                    conn.sendall(b"Stop.endmes")
                        
                else:
                    print("hi")
               
        

            