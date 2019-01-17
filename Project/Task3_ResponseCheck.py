# Project  Task 3 
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

# This will send one attempted packet to each port to verify response times
import socket 
import sys
from scapy.all import *
import time
import random

dest_ip = "10.12.1.141"
dest_port = 2600
source_ip = "10.204.0.68"

source_ports = [3, 33, 333, 3333, 33333]
message = "Ethan Hunt 0"
packets = []
for item in source_ports:
	packets.append( IP(dst=dest_ip,src=source_ip)/UDP(dport=dest_port, sport=item)/message)

print("Sending packets")
sr(packets, inter = 0)
ans.summary()
