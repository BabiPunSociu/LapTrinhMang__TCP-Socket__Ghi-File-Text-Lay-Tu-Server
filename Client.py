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
    sk.connect((ip, port))
    data = 'hello server'
    # Gui 1
    sk.send(data.encode('utf-8'))
    # Ghi du lieu vao file filename
    filename = 'send1.txt'
    with open(filename, 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = sk.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            f.write(data)
    f.close()
    data = sk.recv(1024)
    print(data.decode('utf-8'))
    sk.close()