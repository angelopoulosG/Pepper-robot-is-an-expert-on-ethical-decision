# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import socket
import sys



serverIp = "127.0.0.1"
messages = ['']
server_address = (serverIp, 10001)

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
            data = s.recv(1024)
            if(data!=check): 	
    
                if(data == 'Begin'):
                    s.send('Begin OK')    
    				
                if(data == 'Camera'):	
                    #camera()
                    s.send("Camera OK")      
    
                if(data == 'Hands'):
                    #move_hands()
                    s.send("Hands OK")    
    
                if(data == 'Stop'):
                    print("bye")                    
                    break


    print >>sys.stderr, 'closing socket', s.getsockname()
    s.close()
    print("----------------------------")