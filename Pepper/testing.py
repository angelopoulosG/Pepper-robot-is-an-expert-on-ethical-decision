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
from os import path





global tts
global ttsa
global audio
global record
global aup
global photoCaptureProxy
global videoRecorderProxy
videoRecorderProxy = photoCaptureProxy = tts = audio = record = aup = None


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

# Function to display hostname and
# IP address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
#===================================================================

porta =9559

session = qi.Session()
session.connect("tcp://" + get_ip() + ":" + str(porta))


tabletService = session.service("ALTabletService")

# Ensure that the tablet wifi is enable
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


#thevalue=menu()
thevalue='a'
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



motion_service = session.service("ALMotion")
tracker_service = session.service("ALTracker")

# First, wake up.
motion_service.wakeUp()

# Add target to track.
targetName = "Face"
faceWidth = 0.1
tracker_service.registerTarget(targetName, faceWidth)

# Then, start tracker.
tracker_service.track(targetName)

print "ALTracker successfully started, now show your face to robot!"





speech('Hello human ^start(animations/Stand/Gestures/Hey_1) I am running some tests.')
time.sleep(2)

speech('^start(animations/Stand/Gestures/Explain_3) I am going to show you an image.')

print "Display a web page on the tablet"

# Display a web page on the tablet
tabletService.showWebview("https://i.ibb.co/fdfXXPz/case1.png")

time.sleep(7)

# Hide the web view
tabletService.hideWebview()
print "Stop Displaying the web page on the tablet"




# Stop tracker.
tracker_service.stopTracker()
tracker_service.unregisterAllTargets()
motion_service.rest()

print "ALTracker stopped."




print "Start QR code reader."

speech('^start(animations/Stand/Gestures/Explain_6) Please show me the image with the qr code.')

time.sleep(2)



barcode_service = session.service("ALBarcodeReader")
memory_service = session.service("ALMemory")

barcode_service.subscribe("test_barcode")
print "The code is:"

# Query last data from ALMemory twenty times
for range_counter in range(20):
    data = memory_service.getData("BarcodeReader/BarcodeDetected")
    print data
    time.sleep(1)
print "Stop QR code reader."
