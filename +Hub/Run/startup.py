import os
import socket
import sys

print("\n---Checking for other Hub!---")
try:
    socket.gethostbyname('hub.local')
    print("Other hub found. Exiting...")
    sys.exit(1)
except socket.error:
    print("Hub not found. Good to go!")

os.system('sudo systemctl enable avahi-daemon && sudo systemctl start avahi-daemon')
