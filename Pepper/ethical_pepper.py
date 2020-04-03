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


    check=0
    # Read responses on both sockets
    for s in socks:
        while True:
            data = s.recv(4096)
            if(data!=check): 	
    
                if(data == b'Begin'):
                    s.send('Begin OK')    
    				
                if(data == b'Camera'):	
                    camera()
                    image = "/var/volatile/image.jpg"
                    bytes = open(image).read()	
                    s.send(str(len(bytes)))	

                if(data == b'ContinueWithCamera'):			
                    s.sendall(bytes)      
    
                if(data == b'Hands'):
                    #move_hands()
                    s.send("Hands OK")    
    
                if(data == b'Stop'):
                    print("bye")                    
                    break


    print >>sys.stderr, 'closing socket', s.getsockname()
    s.close()
    print("----------------------------")
