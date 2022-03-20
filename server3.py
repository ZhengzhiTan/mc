# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 08:07:20 2022

@author: 11417
"""

import socket, ssl

def deal_with_client(connstream):
    data = connstream.recv(1024)
    # empty data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.recv(1024)
    # finished with client


server_address = ('127.0.0.1',6666)

cxt = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
cxt.load_cert_chain(certfile="rsa.crt", keyfile="rsa.key")

with socket.socket() as socket: 
    socket.bind(server_address)
    socket.listen(5)
    with 


while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
        
        