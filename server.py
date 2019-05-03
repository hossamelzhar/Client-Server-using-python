#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 06:23:11 2019

@author: elzhar
"""

from socket import *

try:
    s= socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    
    host="127.0.0.1"
    port=5000
    
    s.bind((host,port))
    s.listen(5)
    c,addr = s.accept()
    
    while True:
        x=c.recv(2048)
        print("client : ",x.decode('utf-8'))
        c.send(input('server :').encode('utf-8'))
    
    s.close()

except error as e:
    print(e)
except KeyboardInterrupt:
    print('chat has finished')
    
