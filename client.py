# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 05:08:43 2022

@author: 11417
"""

import socket

MAX_BYTES = 4096

with socket.socket(socket.AF_socket,socket,
                   socket.SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1',6666))
    sock.sendall(b'hello')
    data = sock.recv(MAX_BYTES)
    print (data)
