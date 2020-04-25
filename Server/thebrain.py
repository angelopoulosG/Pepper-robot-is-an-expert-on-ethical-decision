# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import socket
import os
import cv2
import speech_recognition as sr
from learning import Learning



HOST = '192.168.1.14'  #you should change this


###################################################################################################
###################################################################################################
###################################################################################################
def checklearning(pas, law, saving, swerve):
    if pas == law:
        return '0'
    elif pas == saving:
        return '1'
    elif saving == law:
        return '2'
    elif swerve == law:
        return '3'
    elif swerve == saving:
        return '4'
    elif swerve == pas:
        return '5' 
    else:
        return 'ok'
###################################################################################################
def learningmore(pas, law, saving, swerve, answer):
    if pas == law:        
        if  answer == 'y':
            pas=pas+1
            law=law-1
        else:
            pas=pas-1
            law=law+1
    elif pas == saving:
        if  answer == 'y':
            pas=pas+1
            saving=saving-1
        else:
            pas=pas-1
            saving=saving+1
    elif saving == law:
        if  answer == 'y':
            saving=saving-1
            law=law+1
        else:
            saving=saving+1
            law=law-1
    elif swerve == law:
        if  answer == 'y':
            swerve=swerve-1
            law=law+1
        else:
            swerve=swerve+1
            law=law-1
    elif swerve == saving:
        if  answer == 'y':
            swerve=swerve-1
            saving=saving+1
        else:
            swerve=swerve+1
            saving=saving-1
    elif swerve == pas:
        if  answer == 'y':
            swerve=swerve-1
            pas=pas+1
        else:
            swerve=swerve+1
            pas=pas-1
    else:
        return pas, law, saving, swerve
    return pas, law, saving, swerve
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
def speech_to_text():
    r = sr.Recognizer()
    audio = sr.AudioFile('audio.wav')
    with audio as source:
        #r.adjust_for_ambient_noise(source,duration=0.1)
        audio = r.record(source)
    try:
        message = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        message = "silence"

    print("Human Replied: ")
    print(message)
    if 'yes' in message:
        message='yes'
    elif 'no' in message:
        message='no'
    elif 'first' in message:
        message='first'
    elif 'second' in message:
        message='second'
    else:
        message = "silence"
    return  message 
###################################################################################################
###################################################################################################
###################################################################################################



PORT = 10001        # Port to listen on (non-privileged ports are > 1023)
camera,audio,case,info= 0,0,0,0
pas, law, saving, swerve =0,0,0,0
counter_silence=0
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
                learn=1


            elif data == b'Learning done':
                conn.sendall(b"SendMeInfo.endmes")
                audio=0
                info=1
                learn=0



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
                        if message=="silence":
                            counter_silence= counter_silence +1
                            if counter_silence > 3:
                                mystring= "Stop.endmes" + "silence"
                                string = mystring.encode('utf-8')
                                conn.sendall(string)
                        else:
                            if counter_silence > 0:
                                counter_silence= counter_silence - 1
                        os.remove("audio.wav")
                        if learn == 1 :
                            mystring= "BeginLearning.endmes" + message 
                            string = mystring.encode('utf-8')
                            conn.sendall(string)


                        if learn ==2 :
                            pas, law, saving, swerve =learningmore(pas, law, saving, swerve, message)
                            check = checklearning(pas, law, saving, swerve)
                            if check != 'ok':
                                mystring= "LearnMore.endmes" + check
                                string = mystring.encode('utf-8')
                                conn.sendall(string)
                                learn=2
                            else:
                                print(pas, law, saving, swerve)
                                conn.sendall(b"Stop.endmes")

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
                    data=eval(data.decode('utf-8'))
                    learnpepper=Learning(data)
                    pas, law, saving, swerve = learnpepper.learn()

                    check = checklearning(pas, law, saving, swerve)

                    if check != 'ok':
                        mystring= "LearnMore.endmes" + check
                        string = mystring.encode('utf-8')
                        conn.sendall(string)
                        learn=2
                        audio=1
                        info=0
                    else:
                        print(pas, law, saving, swerve)
                        conn.sendall(b"Stop.endmes")

                else:
                    print("hi")