# heartBeat RFC
# Capt Arif Alamri 
# Lt Micah Hayden
# Lt Lucas Mireles

import socket 
import sys
from scapy.all import *
import time
import random

dest_ip = "10.1.8.96"
dest_port = 45434
source_ip = "10.204.0.5"
message = "500\x08ihavenotsleptyet"
packet = ( IP(dst=dest_ip,src=source_ip)/TCP(dport=dest_port, flags='S')/message)
send(packet, inter = 60)