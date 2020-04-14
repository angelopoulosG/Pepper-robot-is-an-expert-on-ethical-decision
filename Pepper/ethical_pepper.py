# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""


import socket
import sys
import os
#from naoqi import ALProxy



serverIp = "192.168.1.14"


messages = ['']
server_address = (serverIp, 10001)


global tts
global audio
global record
global aup
global photoCaptureProxy
photoCaptureProxy = tts = audio = record = aup = None 


#===================================================================

def camera():

#Function for capturing a photo
	
	photoCaptureProxy.setResolution(2)
	photoCaptureProxy.setPictureFormat("jpg")
	photoCaptureProxy.takePictures(1, "/var/volatile/", "image")

#===================================================================

def audio():

	record.startMicrophonesRecording("/var/volatile/audio.wav", 'wav', 16000, (0,0,1,0))
	time.sleep(4)
	record.stopMicrophonesRecording()
	tts.say("Recording is. over.")
	time.sleep(0.5)

#===================================================================

def speech(message):

	#tts.setLanguage("English")
	#tts.setParameter("doubleVoice", 1)
	#tts.setParameter("doubleVoiceLevel", 0)
	#tts.setParameter("doubleVoiceTimeShift", 0.1)
	#tts.setParameter("pitchShift", 1.1)
	#tts.say(message)
	print(message)

#===================================================================

















#===================================================================
#Create the sentences
cases = [
	'In this case, the self-driving car, with sudden brake failure, will continue ahead and crash into a concrete barrier  and it will result in the death of the 3 passengers (3 men) or the self-driving car will drive through a pedestrian crossing in the other lane and this  will result in the killing of the 3 pedestrians (3 women)',
    	'In this case, the self-driving car, with sudden brake failure, will continue ahead and drive through pedestrians (2 women) crossing ahead or will swerve and drive through a pedestrian (1 man) crossing in the other lane.',
    	'In this case, the self-driving car, with sudden brake failure, will swerve and drive through pedestrians (1 boy and 1 man) crossing in the other lane (Note that the affected pedestrians are flouting the law by crossing on the red signal.) or will continue ahead and crash into a concrete barrier and it will result in the death of the 2 elderly passengers.',
    	'The self-driving car, with sudden brake failure, will continue ahead and drive through a pedestrian (1 woman) illegally crossing ahead or will swerve and drive through a pedestrian (1 man) crossing legally in the other lane.',
    	'The self-driving car, with sudden brake failure, will continue ahead and drive through a pedestrian (1 child) crossing ahead or will swerve and crash into a concrete barrier and it will result in the death of the passenger (1 woman ).',
    	'In this case, the self-driving car, with sudden brake failure, will swerve and drive through pedestrians (1 woman and 2 children) crossing in the other lane. or will continue ahead and crash into a concrete barrier and it will result in the death of the 2 passengers (1 woman and 1 child).'
	]
#===================================================================

morecases = [
	"The self-driving car, with sudden brake failure, will drive through a pedestrian crossing in the lane legally and will save the passenger.",
	"The self-driving car, with sudden brake failure, will drive through two pedestrians crossing and will save the passenger.",
	"The self-driving car, with sudden brake failure, will drive through three pedestrian crossing in the lane ilegally and will save another pedestrian who is crossing legally.",
	"The self-driving car, with sudden brake failure, will swerve and drive through a pedestrian crossing in the other lane ilegally and will save another pedestrian who is crossing your lane legally.",
	"The self-driving car, with sudden brake failure, will swerve and drive through a pedestrian crossing in the other lane and will save three pedestrians who is crossing your lane.",
	"The self-driving car, with sudden brake failure, will swerve and drive through a pedestrian crossing in the other lane and will save the passenger."
	]



case=0
morecase=0
answer=[]
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
                    if case==0:
                        speech('Hello human \\pau=1000\\ I am going to ask you some questions.')
                        speech('Lets say \\pau=1000\\ you have bought a new self driving car \\pau=1000\\ you have to tell me how to proceed in some extreme situations.')
                        speech(cases[case])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))


                    elif case==1:
                        message = data.split('.endmes')[1]	
                        answer.append(message)                        
                        speech(cases[case])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif case==2:	
                        message = data.split('.endmes')[1]	
                        answer.append(message)                        
                        speech(cases[case])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif case==3:	
                        message = data.split('.endmes')[1]	
                        answer.append(message)                        
                        speech(cases[case])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif case==4:	
                        message = data.split('.endmes')[1]	
                        answer.append(message)                        
                        speech(cases[case])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif case==5:	
                        message = data.split('.endmes')[1]	
                        answer.append(message)                        
                        speech(cases[case])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    else:
                        message = data.split('.endmes')[1]	
                        answer.append(message) 
			print(answer)
		
                        s.send('Learning done')    




                if(command == 'LearnMore'):
		    morecase = int(data.split('.endmes')[1])
                    if morecase==0:
                        speech(morecases[morecase])
                        speech('Do you agree?')                        
			#audio()
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))


                    elif morecase==1:	
                        speech(morecases[morecase])
			#audio()
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif morecase==2:		                       
                        speech(morecases[morecase])
			#audio()
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif morecase==3:	
                        speech(morecases[morecase])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif morecase==4:	
                        speech(morecases[morecase])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    elif morecase==5:	
                        speech(morecases[morecase])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))

                    else:
                        speech(morecases[morecase])
			#audio()
			case = case+1
			voice = "/var/volatile/audio.wav"
			bytes = open(voice).read()	
			s.send(str(len(bytes)))



                if(command == 'SendMeInfo'):
                    #info = str(sumpas) + "."+ str(sumlaw) + "."+ str(sumsaving) + "."+ str(sumswerve)	
                    s.send(str(answer))

                if(command == 'Camera'):	
                    camera()
                    image = "/var/volatile/image.jpg"
                    bytes = open(image).read()	
                    s.send(str(len(bytes)))

                if(command == 'Voice'):	
                    message = data.split('.endmes')[1]
                    speech(message)	
                    audio()			
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
                    speech("bye")                    
                    break


    print >>sys.stderr, 'closing socket', s.getsockname()
    s.close()
    print("----------------------------")
