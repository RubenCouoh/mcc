# -*- coding: utf-8 -*-
# @Author: 
#          Rubén Couoh
#          Reyna Ay  
#          Luis Rodriguez

import socket

HOST = 'localhost'
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UTP

print('Número aleatorio entre [a, b]')
print('a b')

while True:

  out = input()
  s.sendto(bytes(out,'utf-8'), (HOST, PORT))
  data, addr = s.recvfrom(1024) # buffer 1024 bytes

  print(data)