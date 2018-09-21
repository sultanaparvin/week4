# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:19:53 2018

@author: Owner
"""


import socket
print('Server')
port = 9500
s = socket.socket()
s.bind(('',port))

s.listen(5)

while True:
    conn, addr = s.accept()
    clientmessage = conn.recv(1024)
    if clientmessage.decode() == "Hello":
        conn.send('Hi'.encode())
    else:
        conn.send('Goodbye'.encode())
    conn.close()