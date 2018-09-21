# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:26:32 2018

@author: Owner
"""

import socket
print('Client')
s = socket.socket()
port = 9500
s.connect(('127.0.0.1',port))
s.send('Hello'.encode())
print(s.recv(1024))
s.close()