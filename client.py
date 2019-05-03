#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:50:13 2019

@author: elzhar
"""

try:
    from socket import *
    s=socket(AF_INET,SOCK_STREAM)
    host="127.0.0.1"
    port=5000
    s.connect((host,port))
    while True:
        s.send(input('client : ').encode('utf-8'))
        y=s.recv(2048)
        print('server : ',y.decode('utf-8'))
    s.close()
    
except error as e:
    print(e)
except KeyboardInterrupt:
    print('chat has finished')
