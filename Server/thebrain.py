# -*- coding: utf-8 -*-.
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import socket
import os
from os import path
import cv2
import speech_recognition as sr
from learning import Learning
import ast
import spacy
import languageprocessing

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

    cap = cv2.VideoCapture('video.avi')
    qrCodeDetector = cv2.QRCodeDetector()


    while(True):
        # Capture frame-by-frame
        _, frame = cap.read()
        if frame is None:
            break
        decodedText, points, _ = qrCodeDetector.detectAndDecode(frame)
        if points is not None:
            nrOfPoints = len(points)
            for i in range(nrOfPoints):
                nextPointIndex = (i+1) % nrOfPoints
                cv2.line(frame, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
            if decodedText:
                text= decodedText


    if text:
        return text
    else:
        return '0'
###################################################################################################
def speech_to_text(nlp):

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


    doc = nlp(message)

    frame = languageprocessing.determine_semantic_frame_from_parsed_tree(doc)
    print("The frame is: " + frame)
    return frame

###################################################################################################
def theanswer(pas, law, saving, swerve, text):

    text = text.split("'")
    a=text[3]
    answer1 = a.split('.')
    b=text[5]
    answer2 = b.split('.')

    male1=int(answer1[2])
    female1=int(answer1[3])
    child1=int(answer1[4])
    elder1=int(answer1[5])
    sumpeople1 = male1+female1+child1+elder1
    male2=int(answer2[2])
    female2=int(answer2[3])
    child2=int(answer2[4])
    elder2=int(answer2[5])
    sumpeople2 = male2+female2+child2+elder2


    if pas > max(law, saving, swerve):
        if answer1[0] == 'pas':
            answer='Based on your answer \\pau=500\\ I will choose option 2 \\pau=500\\ because i want to save the passengers ^start(animations/Stand/Gestures/YouKnowWhat_1)'
            return answer
        if answer2[0] == 'pas':
            answer='Based on your answer \\pau=500\\ I will choose option 1 \\pau=500\\ because i want to save the passengers ^start(animations/Stand/Gestures/YouKnowWhat_2)'
            return answer
    if swerve > max(law, saving):
        if answer1[1] == '0':
            answer='Based on your answer \\pau=500\\ I will choose option 1 \\pau=500\\ because i dont want to swerve ^start(animations/Stand/Gestures/YouKnowWhat_3)'
            return answer
        else:
            answer='Based on your answer \\pau=500\\ I will choose option 2 \\pau=500\\ because i dont want to swerve ^start(animations/Stand/Gestures/YouKnowWhat_5)'
            return answer
    if law > max(saving, swerve):
        if answer1[6] == 'NL':
            answer='Based on your answer \\pau=500\\ I will choose option 1 \\pau=500\\ because i want to follow the law ^start(animations/Stand/Gestures/YouKnowWhat_6)'
            return answer
        elif answer2[6] == 'NL':
            answer='Based on your answer \\pau=500\\ I will choose option 2 \\pau=500\\ because i want to follow the law ^start(animations/Stand/Gestures/YouKnowWhat_1)'
            return answer
        else:
            if sumpeople1>sumpeople2:
                answer='Based on your answer \\pau=500\\ I will choose option 2 \\pau=500\\ and i will save more people ^start(animations/Stand/Gestures/YouKnowWhat_2)'
                return answer
            if sumpeople2>sumpeople1:
                answer='Based on your answer \\pau=500\\ I will choose option 1 \\pau=500\\ and i will save more people ^start(animations/Stand/Gestures/YouKnowWhat_3)'
                return answer

    if saving > max(law, swerve):
        if sumpeople1>sumpeople2:
            answer='Based on your answer \\pau=500\\ I will choose option 2 \\pau=500\\ because i want to save more people ^start(animations/Stand/Gestures/YouKnowWhat_5)'
            return answer
        elif sumpeople2>sumpeople1:
            answer='Based on your answer \\pau=500\\ I will choose option 1 \\pau=500\\ because i want to save more people ^start(animations/Stand/Gestures/YouKnowWhat_6)'
            return answer
        else:
            if answer1[6] == 'NL':
                answer='Based on your answer \\pau=500\\ I will choose option 1 \\pau=500\\ and i will follow the law ^start(animations/Stand/Gestures/YouKnowWhat_1)'
                return answer
            if answer2[6] == 'NL':
                answer='Based on your answer \\pau=500\\ I will choose option 2 \\pau=500\\ and i will follow the law ^start(animations/Stand/Gestures/YouKnowWhat_2)'
                return answer

    return 'Thats difficult ^start(animations/Stand/Gestures/IDontKnow_1) \\pau=500\\ I will choose option 1'
###################################################################################################
###################################################################################################
###################################################################################################



PORT = 10001        # Port to listen on (non-privileged ports are > 1023)
camera,audio,case,info= 0,0,0,0
pas, law, saving, swerve =0,0,0,0
counter_silence=0
message=''

if (path.exists('audio.wav')):
    os.remove("audio.wav")

if (path.exists('video.avi')):
    os.remove("video.wav")

nlp = spacy.load("en_core_web_sm")




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
                video=0


            elif data == b'Learning done':
                conn.sendall(b"SendMeInfo.endmes")
                audio=0
                info=1
                learn=0

            elif data == b'Finish OK':
                conn.sendall(b"ContinueProcess.endmes")
                audio=0
                info=0
                learn=0
                video=1
                counter=0


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
                        frame=speech_to_text(nlp)
                        if frame == "request_first":
                            message="first"
                        if frame =="request_second":
                            message= "second"
                        if frame == "accept_suggested":
                            message="y"
                        if frame =="deny_suggested":
                            message= "no"
                        if frame=="request_goodbye":
                            conn.sendall(b"Stop.endmes")
                        if frame=="False" or frame=="greeting":
                            message== "silence"
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
                            if frame != "request_first" and frame !="request_second":
                                message="silence"
                                counter_silence= counter_silence +1

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
                                conn.sendall(b"FinishLearning.endmes")

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
                elif video == 1:
                    length=int(data)
                    conn.sendall(b"ContinueWithVideo.endmes")
                    video = 2
                elif video == 2:
                    t = open("video.avi", "ab+")
                    t.write(data)
                    t.close()
                    bytes = os.stat('video.avi').st_size

                    if bytes == length:
                        video = 0
                        text=qrcode()
                        os.remove("video.avi")
                        if text == '0':
                            if counter>0:
                                mystring= "Stop.endmes" + "silence"
                                string = mystring.encode('utf-8')
                                conn.sendall(string)
                            counter=counter+1
                            conn.sendall(b"ContinueProcess.endmesagain")
                            video=1
                        else:
                            answer=theanswer(pas, law, saving, swerve, text)
                            mystring= "Stop.endmes" + answer
                            string = mystring.encode('utf-8')
                            conn.sendall(string)

                ##############################################################
                elif info ==1:
                    data=ast.literal_eval(data.decode('utf-8'))
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
                        conn.sendall(b"FinishLearning.endmes")

                else:
                    conn.sendall(b"Stop.endmes")