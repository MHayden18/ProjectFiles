# Project  Task 3 
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

# This will send one attempted packet to each port to verify times
import socket 
import sys
from scapy.all import *
import time
import random

dest_ip = "10.12.1.1"
dest_port = 1337
source_ip = "10.204.0.67"
message = "Deactivate!!"
packets = []
for i in range (5018):
	packets.append( IP(dst=dest_ip,src=source_ip)/UDP(dport=dest_port, sport=random.randint(1024,65535))/message)
	
send(packets, inter = 0)