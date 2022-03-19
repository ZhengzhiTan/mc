# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 05:08:44 2022

@author: 11417
"""

import socket
from time import sleep

MAX_BYTES = 4096

with socket.socket(socket.AF_INET,
                   socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 6666))
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(MAX_BYTES)
    print (data)
    sleep(5)
    conn.sendall(b'received')
    conn.close()
    