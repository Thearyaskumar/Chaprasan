import os

print("\n\n---Installing Avahi---")
os.system('sudo apt-get install avahi-daemon -y')
os.system('sudo systemctl enable avahi-daemon; sudo systemctl stop avahi-daemon')

print("\n\n---Configuring installation file---")
DeviceName = os.popen('cd .. && basename "$PWD"').read()[1:].lower()

#Remove existing config:
os.system('rm -Rf /etc/avahi/* && cp ./avahi-daemon.conf /etc/avahi/')

#Editing the config:
with open('/etc/avahi/avahi-daemon.conf', 'r') as file:
    data = file.readlines()

print(data[21])
data[21] = 'host-name=' + DeviceName + '\n'

# and write everything back
with open('/etc/avahi/avahi-daemon.conf', 'w') as file:
    file.writelines( data )
