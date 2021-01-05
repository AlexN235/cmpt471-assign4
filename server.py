#!/usr/bin/env python

import socket
import MultiEncryption as ME

HOST = "127.0.0.1" # loopback addr
PORT = 45678
privateNum = 4
message = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break   
            message += data.decode("utf-8")       
            conn.sendall(data)
   
hiddenKey = int(message[:1])
key = ME.computeKeyDecrypt(hiddenKey, privateNum)

string = str(message[1:])
order = ME.getSchemeOrder(key)
print(ME.Decrypt(string, order))

