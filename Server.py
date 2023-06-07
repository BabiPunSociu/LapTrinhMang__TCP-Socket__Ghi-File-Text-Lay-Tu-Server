# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:39:40 2023

@author: ADMIN
"""

import socket

if __name__ == '__main__':
    ip = 'localhost'
    port = 9050
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((ip, port))
    sk.listen(5)
    print('waiting...')
    while True:
        client_sk, client_add = sk.accept()
        print('client address', client_add)
        # Nhan 1
        data = client_sk.recv(1024)
        print('receive', repr(data))
        filename = 'send.txt'
        # Doc file
        f = open(filename, 'rb')
        l = f.read(1024)
        while l:
            client_sk.send(l)
            print('sent', repr(l))
            l = f.read(1024)
        f.close()
        print('done')
        client_sk.send('finish'.encode('utf-8'))
        client_sk.close()