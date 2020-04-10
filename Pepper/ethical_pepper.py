# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import learning
import socket
import sys
import os
from naoqi import ALProxy



serverIp = "192.168.1.14"
messages = ['']
server_address = (serverIp, 10001)




#===================================================================

def camera():

#Function for capturing a photo

	# Create a proxy to ALPhotoCapture
	try:
	  photoCaptureProxy = ALProxy("ALPhotoCapture", "127.0.0.1", 9559)
	except Exception, e:
	  print "Error when creating ALPhotoCapture proxy:"
	  print str(e)
	  exit(1)	
	photoCaptureProxy.setResolution(2)
	photoCaptureProxy.setPictureFormat("jpg")
	photoCaptureProxy.takePictures(1, "/var/volatile/", "image")

#===================================================================

def audio(message):

#Function for audio player and for recording
	tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
	audio = ALProxy("ALAudioDevice", "127.0.0.1", 9559)
	record = ALProxy("ALAudioRecorder", "127.0.0.1", 9559)
	aup = ALProxy("ALAudioPlayer", "127.0.0.1", 9559)


	tts.setParameter("doubleVoice", 1)
	tts.setParameter("doubleVoiceLevel", 0)
	tts.setParameter("doubleVoiceTimeShift", 0.1)
	tts.setParameter("pitchShift", 1.1)
	tts.say(message)
	record.startMicrophonesRecording("/var/volatile/audio.wav", 'wav', 16000, (0,0,1,0))
	time.sleep(3)
	record.stopMicrophonesRecording()
	tts.say("Recording is. over.")
	time.sleep(1)

#===================================================================



# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM)]


print >>sys.stderr, 'connecting to %s port %s' % server_address


for s in socks:
    s.connect(server_address)
    print("----------------------------")



for message in messages:

    # Send messages on both sockets
    for s in socks:
        s.send("Ready")


    # Read responses on both sockets
    for s in socks:
        while True:
            data = s.recv(4096)
            if(data!= 0):


	    	command = data.split('.endmes')[0]
                if(command == 'BeginLearning'):
                    learningfunction()		
                    s.send('Begin OK')    

                if(command == 'Camera'):	
                    camera()
                    image = "/var/volatile/image.jpg"
                    bytes = open(image).read()	
                    s.send(str(len(bytes)))

                if(command == 'Voice'):	
                    message = data.split('.endmes')[1]
                    print(message)	
                    audio(message)			
                    voice = "/var/volatile/audio.wav"
                    bytes = open(voice).read()	
                    s.send(str(len(bytes)))	

                if(command == 'ContinueWithCamera'):			
                    s.sendall(bytes)      

                if(command == 'ContinueWithVoice'):			
                    s.sendall(bytes)  
    
                if(command == 'Hands'):
                    #move_hands()
                    s.send("Hands OK")    
    
                if(command == 'Stop'):
                    print("bye")                    
                    break


    print >>sys.stderr, 'closing socket', s.getsockname()
    s.close()
    print("----------------------------")
