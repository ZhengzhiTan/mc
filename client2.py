# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 07:05:22 2022

@author: 11417
"""

import socket
import ssl

server_address = ('127.0.0.1',6666)

cxt = ssl._create_unverified_context()

with socket.socket() as sock:
    with cxt.wrap_socket(sock,server_hostname=server_address[0]) as ssock:
        ssock.connect(server_address)
        print(f'local address: {ssock.getsockname()}')
        ssock.send('hello'.encode())
        print(ssock.recv(1024).decode())
        ssock.close()