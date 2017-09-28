# -*- coding: utf-8 -*-
# @Author: 
#          Rubén Couoh
#					 Reyna Ay  
#					 Luis Rodriguez

import socket

HOST = ''
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Cliente conectado:', addr)

while True:
  data = str(conn.recv(1024), 'utf8') # buffer 1024 bytes

  if not data: break
  print(addr, data)

  string, count = data.split(" ")
  out = data + ' = ' + string * int(count)

  conn.sendall(bytes(out, 'utf-8'))