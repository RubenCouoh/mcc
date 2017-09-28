# -*- coding: utf-8 -*-
# @Author: 
#          Rubén Couoh
#          Reyna Ay  
#          Luis Rodriguez

import socket
import random

HOST = ''
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
s.bind((HOST, PORT))

while True:
  data, addr = s.recvfrom(1024) # buffer 1024 bytes
  data = str(data, 'utf-8')
  if not data: break

  print(addr, data)

  a, b = data.split(" ")
  rand = random.randint(int(a), int(b))
  out = 'randon(' + a +', '+ b+ ') = ' + str(rand)

  s.sendto(bytes(out, 'utf-8'), addr)