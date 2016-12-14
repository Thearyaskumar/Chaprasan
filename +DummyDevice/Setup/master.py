import os
print("\nRunning dummy device script!")
os.system('sudo apt-get install avahi-daemon -y')
os.system('sudo systemctl enable avahi-daemon; sudo systemctl start avahi-daemon')
