# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 06:55:26 2022

@author: 11417
"""

import socket
import ssl
# 创建上下文
cxt = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
cxt.load_default_certs(ssl.Purpose.CLIENT_AUTH)
##证书
cxt.load_cert_chain(certfile='',='')
server_address = ('127.0.0.1',6666)

with socket.socket(socket.AF_INET,
                   socket.SOCK_STREAM) as sock:
    ##绑定本地地址
    sock.bind((server_address))
    ##监听
    sock.listen(1)
    with cxt.wrap_socket(sock,server_side=True) as ssock:
        while True:
            conn, addr = ssock.accept()
            print(f'local server adress: {ssock,getsockname()}')
            print(f'client address: {addr}')
            print(conn.recv(1024).decode())
            conn.sends(b'received')
            conn.close()