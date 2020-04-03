# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import socket




HOST = '192.168.1.14'  # Standard loopback interface address (localhost)
PORT = 10001        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data == b'Ready':
                conn.sendall(b"Begin")
            else:
                print(data)
                if data == b'Begin OK':
                    conn.sendall(b"Camera")
                elif data == b'Camera OK':
                    conn.sendall(b"Hands")
                elif data == b'Hands OK':
                    conn.sendall(b"Stop")
                else:
                    print("HI")
            