# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 08:03:56 2022

@author: 11417
"""
import socket
import ssl
context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("rsa.crt")
conn = context.wrap_socket(socket.socket(socket.AF_INET),
                           server_hostname="127.0.0.1")
conn.connect(("127.0.0.1", 6666))
cert = conn.getpeercert()
print(cert)
conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
print(conn.recv(1024).split(b"\r\n"))