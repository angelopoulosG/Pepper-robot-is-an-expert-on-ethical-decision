# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:01:44 2020

@author: Georgios Angelopoulos
"""

import socket
import os
import cv2



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
        print(decodedText)     

    else:
        print("QR code not detected")
###################################################################################################
        
        

HOST = '192.168.1.14'  # Standard loopback interface address (localhost)
PORT = 10001        # Port to listen on (non-privileged ports are > 1023)
length= 0
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
                conn.sendall(b"Begin")
            elif data == b'Begin OK':
                conn.sendall(b"Camera")
                camera=1
            elif data == b'Hands OK':
                conn.sendall(b"Stop")
            else:

                if camera == 2:
                    t = open("image.jpg", "ab+")
                    t.write(data)
                    t.close()
                    bytes = os.stat('image.jpg').st_size
                    print(bytes)
                    if bytes == length:
                        camera = 0                   
                        qrcode()
                        os.remove("image.jpg")
                        conn.sendall(b"Hands")
                if camera == 1:
                    length=int(data)
                    print(length)

                    string=0
                    conn.sendall(b"ContinueWithCamera")                    
                    camera = 2                        
        

            