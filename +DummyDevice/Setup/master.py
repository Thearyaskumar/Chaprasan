import os
print("\nRunning dummy device script!")
os.system('sudo apt-get install avahi-daemon -y')
os.system('sudo systemctl enable avahi-daemon; sudo systemctl stop avahi-daemon')
os.system('rm /etc/avahi/avahi-daemon.conf && cp ./avahi-daemon.conf /etc/avahi/avahi-daemon.conf')
