#!/usr/bin/env python

import socket
import MultiEncryption as ME

HOST = "127.0.0.1" # loopback addr
PORT = 45678
privateNum = 6

string = "Hello World!"

hiddenKey = ME.computeKeyEncrypt(privateNum)
key = ME.computeKeyDecrypt(hiddenKey, 6)
order = ME.getSchemeOrder(key)

toSend = ME.Encrypt(string, order)
body = str(hiddenKey) + toSend

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(body.encode('utf-8'))
    data = sock.recv(1024)
    
    print('Received', repr(str(data)))
    