# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 08:14:59 2022

@author: 11417
"""
import socket
import ssl

server_address = ('127.0.0.1',6666)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='rsa.crt',keyfile='rsa.key')



with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(server_address)
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            conn, addr = ssock.accept() 
            print(f'local server adress: {ssock.getsockname()}')
            print(f'client address: {addr}')
            while True:    
                text = input('my type:')
                if text == 'q':
                    break
                conn.send(text.encode())
                print('client:', conn.recv(1024).decode())
        conn.close()
            