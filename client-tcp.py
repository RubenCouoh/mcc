# -*- coding: utf-8 -*-
# @Author: 
#          Rubén Couoh
#					 Reyna Ay  
#					 Luis Rodriguez

import socket

HOST = 'localhost'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.connect((HOST, PORT))

print('Repite una cadena n veces')
print('Cadena veces')

while True:

  out = input()
  s.sendall(bytes(out,'utf-8'))
  data = str(s.recv(1024), 'utf-8') # buffer 1024 bytes

  print(data)