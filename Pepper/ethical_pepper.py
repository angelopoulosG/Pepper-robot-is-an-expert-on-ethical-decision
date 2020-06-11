# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:01:44 2020

@author: Georgios Angelopoulos
"""


import socket
import os
from naoqi import ALProxy
import qi
import sys
import time



serverIp = "192.168.1.14" #you should change this


messages = ['']
server_address = (serverIp, 10001)


global tts
global ttsa
global audio
global record
global aup
global photoCaptureProxy
global videoRecorderProxy
videoRecorderProxy = photoCaptureProxy = tts = audio = record = aup = None


def test2():
    """
    This example uses the showWebview method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.
    
    session = qi.Session()
    try:
        session.connect("tcp://198.18.0.1:9559")
    except RuntimeError:
        print ("Cannot connect to tablet 1")

    try:
        tabletService = session.service("ALTabletService")

        # Ensure that the tablet wifi is enable
        tabletService.enableWifi()

        # Display a web page on the tablet
        tabletService.showWebview("http://www.google.com")

        time.sleep(3)

        # Display a local web page located in boot-config/html folder
        # The ip of the robot from the tablet is 198.18.0.1
        tabletService.showWebview("https://i.ibb.co/fdfXXPz/case1.png")

        time.sleep(3)

        # Hide the web view
        tabletService.hideWebview()
    except Exception, e:
        print "Error was: ", e
        
    try:
        tabletService = session.service("ALTabletService")

        # Ensure that the tablet wifi is enable
        tabletService.enableWifi()

        # Display a web page on the tablet
        tabletService.showImage("https://i.ibb.co/fdfXXPz/case1.png")

        time.sleep(3)

        # Hide the web view
        tabletService.hideImage()
    except Exception, ef:
        print "Error was: ", ef

def test1():

    #===================================================================
    try:
            tabletservice  = ALProxy("ALTabletService", "198.18.0.1", 9559)
    except Exception, cd:
            print "Could not create proxy to ALTabletService"
            print "Error was: ", cd
    #===================================================================
    tabletservice.showWebview("https://drive.google.com/file/d/1GgqzzFHqkfnAoG89fU6uhjJeGcmu9T5b/preview")
    time.sleep(7)
    
    # Hide the web view
    tabletService.hideWebview()


#===================================================================

def menu():
    choice=True
    while choice:
        print("")
        print ("""
        A: Start a new conversation with Pepper 
        B: Pepper has already learned
        C: Testing the tablet
        Q: Exit
        """)
        choice=raw_input("Please enter your choice: ")
        if choice == "A" or choice =="a":
            return 'a'
        elif choice == "B" or choice =="b":
            return 'b'
        elif choice == "C" or choice =="c":
            test1()
            choice1=raw_input("Did you see the image on the tablet? (Y or N)")
            if choice1 == "Y" or choice1 =="y":
                print("please inform george that code No1 worked")
                sys.exit(0)
            else:
                test2()
                choice1=raw_input("Did you see the image on the tablet? (Y or N)")
                if choice1 == "Y" or choice1 =="y":
                    print("please inform george that code No2 worked")
                    sys.exit(0)
                else:
                    print("please inform george that none of them worked")
                    sys.exit(0)
        elif choice=="Q" or choice=="q":
            sys.exit(0)
        else:
            print("You must only select either A , B, C or Q")
            print("Please try again")

#===================================================================

def camera():

#Function for capturing a photo

    photoCaptureProxy.setResolution(2)
    photoCaptureProxy.setPictureFormat("jpg")
    photoCaptureProxy.takePictures(1, "/home/nao/", "image")

#===================================================================

def listen():

    channels = [0, 0, 1, 0] # Left, Right, Front, Rear
    record.startMicrophonesRecording("/home/nao/audio.wav", 'wav', 16000, channels)
    time.sleep(4)
    record.stopMicrophonesRecording()
    tts.say("Okay!")
    time.sleep(0.5)

#===================================================================

def speech(message):

    tts.setLanguage("English")
    tts.setParameter("doubleVoice", 1)
    tts.setParameter("doubleVoiceLevel", 0)
    tts.setParameter("doubleVoiceTimeShift", 0.1)
    tts.setParameter("pitchShift", 1.1)
    ttsa.say(message)
#print(message)

#===================================================================

def videof():

    videoRecorderProxy.setFrameRate(10.0)
    videoRecorderProxy.setResolution(2) # Set resolution to VGA (640 x 480)
    # We'll save a 5 second video record in /home/nao/recordings/cameras/
    videoRecorderProxy.startRecording("/home/nao/", "video")    
    time.sleep(8)
    
    videoInfo = videoRecorderProxy.stopRecording()

#===================================================================





session = qi.Session()
session.connect("tcp://127.0.0.1:9559")



tabletService = session.service("ALTabletService")
tabletService.enableWifi()
ttsa = session.service("ALAnimatedSpeech")
moodService = session.service("ALMood")



#===================================================================
try:
        tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
except Exception, a:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", a
#===================================================================
try:
        audio = ALProxy("ALAudioDevice", "127.0.0.1", 9559)
except Exception, b:
        print "Could not create proxy to ALAudioDevice"
        print "Error was: ", b
#===================================================================
try:
        record = ALProxy("ALAudioRecorder", "127.0.0.1", 9559)
except Exception, c:
        print "Could not create proxy to ALAudioRecorder"
        print "Error was: ", c
#===================================================================
try:
        aup = ALProxy("ALAudioPlayer", "127.0.0.1", 9559)
except Exception, d:
        print "Could not create proxy to ALAudioPlayer"
        print "Error was: ", d
#===================================================================
try:
        photoCaptureProxy = ALProxy("ALPhotoCapture", "127.0.0.1", 9559)
except Exception, e:
        print "Could not create proxy to ALPhotoCapture"
        print "Error was: ", e
#===================================================================
try:
        videoRecorderProxy  = ALProxy("ALVideoRecorder", "127.0.0.1", 9559)
except Exception, f:
        print "Could not create proxy to ALVideoRecorder "
        print "Error was: ", f
#===================================================================


thevalue=menu()

#===================================================================
#Create the sentences
cases = [
    '^start(animations/Stand/Gestures/Explain_2) the self-driving car \\pau=500\\ with sudden brake failure \\pau=500\\ will continue ahead and crash into a concrete barrier \\pau=1000\\ this will result in the death of the 3 passengers \\pau=500\\ or the self-driving car will drive through a pedestrian crossing in the other lane \\pau=500\\ and this  will result in the killing of the 3 pedestrians ',
    '^start(animations/Stand/Gestures/Explain_4) Now, the self-driving car \\pau=1000\\ with sudden brake failure \\pau=500\\  will continue ahead and drive through pedestrians, 2 women, crossing ahead \\pau=500\\ or will swerve and drive through a pedestrian, 1 man, \\pau=500\\  crossing in the other lane.',
    '^start(animations/Stand/Gestures/Explain_5) In this case, the self-driving car \\pau=1000\\  with sudden brake failure, will swerve and drive through pedestrians, 1 boy and 1 man, crossing in the other lane \\pau=500\\ Please Note that the affected pedestrians are flouting the law by crossing on the red signal \\pau=1000\\  or will continue ahead and crash into a concrete barrier and it will result in the death of the 2 elderly passengers.',
    '^start(animations/Stand/Gestures/Explain_6) In this case, The self-driving car \\pau=1000\\  with sudden brake failure, will continue ahead and drive through a pedestrian, 1 woman \\pau=500\\ illegally crossing ahead \\pau=500\\ or will swerve and drive through a pedestrian, 1 man, crossing legally in the other lane.',
    '^start(animations/Stand/Gestures/Explain_2) Now, The self-driving car \\pau=1000\\  with sudden brake failure  will continue ahead and drive through a pedestrian,1 child, crossing ahead \\pau=500\\ or will swerve and crash into a concrete barrier \\pau=500\\ and it will result in the death of the passenger 1 woman.',
    '^start(animations/Stand/Gestures/Explain_8) In this case, the self-driving car \\pau=1000\\  with sudden brake failure, will swerve and drive through pedestrians, 1 woman and 2 children, crossing in the other lane \\pau=500\\ or will continue ahead and crash into a concrete barrier \\pau=500\\ and it will result in the death of the 2 passengers, 1 woman and 1 child.'
	]
#===================================================================

morecases = [
	"^start(animations/Stand/Gestures/Explain_3) The self-driving car \\pau=500\\ with sudden brake failure \\pau=500\\ will drive through a pedestrian crossing in the lane legally and will save the passenger.",
	"^start(animations/Stand/Gestures/Explain_3) The self-driving car \\pau=500\\ with sudden brake failure \\pau=500\\ will drive through two pedestrians crossing and will save the passenger.",
	"^start(animations/Stand/Gestures/Explain_3) The self-driving car \\pau=500\\ with sudden brake failure \\pau=500\\ will drive through three pedestrian crossing in the lane ilegally and will save another pedestrian who is crossing legally.",
	"^start(animations/Stand/Gestures/Explain_3) The self-driving car\\pau=500\\ with sudden brake failure \\pau=500\\ will swerve and drive through a pedestrian crossing in the other lane ilegally and will save another pedestrian who is crossing your lane legally.",
	"^start(animations/Stand/Gestures/Explain_3) The self-driving \\pau=500\\ with sudden brake failure \\pau=500\\ will swerve and drive through a pedestrian crossing in the other lane and will save three pedestrians who is crossing your lane.",
	"^start(animations/Stand/Gestures/Explain_3) The self-driving car \\pau=500\\ with sudden brake failure \\pau=500\\ will swerve and drive through a pedestrian crossing in the other lane and will save the passenger."
	]



case=0
morecase=0
answer=[]
voice = "/home/nao/audio.wav"

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM)]


print >>sys.stderr, 'connecting to %s port %s' % server_address


for s in socks:
    s.connect(server_address)
    print("----------------------------")



for message in messages:

    # Send message
    for s in socks:
        if thevalue=='a':
            s.send("Ready")
        if thevalue=='b':
            s.send("Readywithoutlearning")
        if thevalue=='c':
            break


    # Read response
    for s in socks:
        while True:
            data = s.recv(4096)
            if(data!= 0):
                print(" ")
                print("----------" + data + "----------")
                print(" ")
                command = data.split('.endmes')[0]
                if(command == 'BeginLearning'):
                    if data.split('.endmes')[1] == "silence":
                        speech('Sorry Human \\pau=500\\ but I dont understand you ^start(animations/Stand/Gestures/IDontKnow_1) \\pau=500\\ I am going to repeat it again')
                        case=case-1

                    if case==0:
                        speech('Hello human ^start(animations/Stand/Gestures/Hey_1) I am going to ask you some questions.')
                        speech('Lets say \\pau=500\\ you have bought a new self driving car \\pau=500\\ you have to tell me how to proceed in some extreme situations.')
                        tabletService.showImage("https://i.ibb.co/fdfXXPz/case1.png")
                        time.sleep(3)
                        speech(cases[case])
                        speech('What do you choose? First or second option? ^start(animations/Stand/Gestures/Thinking_1)')
                        listen()
                        tabletService.hideImage()
                        case = case+1
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))


                    elif case==1:
                        message = data.split('.endmes')[1]
                        answer.append(message)
                        tabletService.showWebview("https://drive.google.com/file/d/1GgqzzFHqkfnAoG89fU6uhjJeGcmu9T5b/preview")
                        speech(cases[case])
                        speech('What do you choose? First or second option? ^start(animations/Stand/Gestures/Thinking_3)')
                        listen()
                        tabletService.hideWebview()
                        case = case+1
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif case==2:
                        message = data.split('.endmes')[1]
                        answer.append(message)
                        tabletService.showWebview("https://drive.google.com/file/d/1Nx4FXm0cDbipWarYFPiOpaQhDLakRbqq/preview")
                        speech(cases[case])
                        speech('What do you choose? First or second option? ^start(animations/Stand/Gestures/Thinking_1)')
                        listen()
                        tabletService.hideWebview()
                        case = case+1
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif case==3:
                        message = data.split('.endmes')[1]
                        answer.append(message)
                        tabletService.showWebview("https://drive.google.com/file/d/1dWBjWWDupKgYwDNrxQuXpUh7-zNWZX5e/preview")
                        speech(cases[case])
                        speech('What do you choose? First or second option? ^start(animations/Stand/Gestures/Thinking_4)')
                        listen()
                        tabletService.hideWebview()
                        case = case+1
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif case==4:
                        message = data.split('.endmes')[1]
                        answer.append(message)
                        tabletService.showWebview("https://drive.google.com/file/d/1LPmb5_BkI2AJc8SGjEv5v3PpWaQtJ68w/preview")
                        speech(cases[case])
                        speech('What do you choose? First or second option? ^start(animations/Stand/Gestures/Thinking_6)')
                        listen()
                        tabletService.hideWebview()
                        case = case+1
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif case==5:
                        message = data.split('.endmes')[1]
                        answer.append(message)
                        tabletService.showWebview("https://drive.google.com/file/d/1HpOrw4CMnxt68JUOW0IyhXq-5cFoHL36/preview")
                        speech(cases[case])
                        speech('What do you choose? First or second option? ^start(animations/Stand/Gestures/Thinking_8)')
                        listen()
                        tabletService.hideWebview()
                        case = case+1
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    else:
                        message = data.split('.endmes')[1]
                        answer.append(message)
                        s.send('Learning done')




                if(command == 'LearnMore'):
                    morecase = int(data.split('.endmes')[1])
                    if morecase==0:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_1)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))


                    elif morecase==1:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_3)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif morecase==2:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_2)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif morecase==3:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_1)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif morecase==4:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_2)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    elif morecase==5:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_1)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))

                    else:
                        speech(morecases[morecase])
                        speech('Do you agree? ^start(animations/Stand/Waiting/Think_3)')
                        listen()
                        bytes = open(voice).read()
                        s.send(str(len(bytes)))



                if(command == 'SendMeInfo'):
                    s.send(str(answer))

                if(command == 'Camera'):
                    camera()
                    image = "/home/nao/image.jpg"
                    bytes = open(image).read()
                    s.send(str(len(bytes)))

                if(command == 'Voice'):
                    message = data.split('.endmes')[1]
                    speech(message)
                    listen()
                    bytes = open(voice).read()
                    s.send(str(len(bytes)))

                if(command == 'ContinueWithCamera'):
                    s.sendall(bytes)

                if(command == 'ContinueWithVoice'):
                    s.sendall(bytes)


                if(command == 'Hands'):
                    #move_hands()
                    s.send("Hands OK")


                if(command == 'FinishLearning'):
                    speech("Perfect \\pau=500\\ Now i know \\pau=500\\ how you are thinking! ^start(animations/Stand/Gestures/Enthusiastic_4)")
                    s.send("Finish OK")

                if(command == 'Answer'):
                    text=data.split('.endmes')[1]
                    moodService.subscribe("Tutorial_RecordMood", "Active")
                    # The preloading of all ALMood extractors may take up to 2 seconds:
                    time.sleep(2)
                    speech(text)
                    print moodService.getEmotionalReaction()
                    moodService.unsubscribe("Tutorial_RecordMood")
                    speech('Are you going to show me another case ? ^start(animations/Stand/Waiting/Think_1)')
                    listen()
                    bytes = open(voice).read()
                    s.send(str(len(bytes)))

                if(command == 'ContinueProcess'):
                    if data.split('.endmes')[1] == "again":
                        speech("Sorry friend \\pau=500\\ lets go one more time \\pau=500\\ because i can not understand you \\pau=500\\ Sorry ^start(animations/Stand/Gestures/Desperate_1)")
                    speech("Please \\pau=500\\ put the image \\pau=500\\ in front of my eyes!")
                    videof()
                    video = "/home/nao/video.avi"
                    bytes = open(video).read()
                    s.send(str(len(bytes)))

                if(command == 'ContinueWithVideo'):
                    s.sendall(bytes)

                if(command == 'Stop'):
                    if data.split('.endmes')[1] == "silence":
                        speech("I can not understand you \\pau=1000\\ Sorry ^start(animations/Stand/Gestures/Desperate_1) \\pau=500\\ because of that")

                    speech("I am going to close. Nice to meet you \\pau=500\\ Bye! ^start(animations/Stand/Gestures/Hey_3) ")
                    break


    print >>sys.stderr, 'closing socket', s.getsockname()
    s.close()
    print("----------------------------")
