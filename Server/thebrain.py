# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import select, socket, sys, Queue



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
# Bind the socket to the port
server_address = ('127.0.0.1', 10001)

print >>sys.stderr, 'starting up on %s port %s' % server_address

server.bind(server_address)
# Listen for incoming connections
server.listen(5)
# Sockets from which we expect to read
inputs = [ server ]
# Sockets to which we expect to write
outputs = [ ]
# Outgoing message queues (socket:Queue)
message_queues = {}



while inputs:
            
    # Wait for at least one of the sockets to be ready for processing
    #print >>sys.stderr, '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:
        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()
        else:
            data=s.recv(1024)
            if data:
                if data == 'Ready':
                    s.send("Begin")
                else:
                    print(data)
                    if data == 'Begin OK':
                        s.send("Camera")
                    elif data == 'Camera OK':
                        s.send("Hands")
                    elif data == 'Hands OK':
                        s.send("Stop")
                    else:
                        print("HI")


                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queues[s]                