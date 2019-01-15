# Project  Task 1
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

import socket 

IP = "hitchhikers.m4i.local"
PORT = 4242
sock = socket.socket(socket.	AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))
sock.sendall(b'\xccWhat is the answer to the Ultimate Question of Life, The Universe, and Everything?')
answer = sock.recv(1024)
print(answer)

sock.close()

