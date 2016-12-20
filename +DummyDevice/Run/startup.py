import os
import socket
import sys

print("\n---Checking for Hub---")
try:
    socket.gethostbyname('hub.local')
except socket.error:
    print("Hub not found. Exiting...")
    sys.exit(1)
