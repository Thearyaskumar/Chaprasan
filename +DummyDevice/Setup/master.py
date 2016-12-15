import os

print("\n---Installing Avahi---\n")
os.system('sudo apt-get install avahi-daemon -y')
os.system('sudo systemctl enable avahi-daemon; sudo systemctl stop avahi-daemon')

print("\n---Configuring installation file---\n")
DeviceName = os.popen('cd .. && basename "$PWD"').read()[1:].lower()

print('Removing existing config...')
os.system('rm -Rf /etc/avahi/* && cp ./avahi-daemon.conf /etc/avahi/')

print('Reading the config...')
with open('/etc/avahi/avahi-daemon.conf', 'r') as file:
    data = file.readlines()

data[21] = 'host-name=' + DeviceName

print('Writing everything back...')
with open('/etc/avahi/avahi-daemon.conf', 'w') as file:
    file.writelines( data )

print('\n---Restarting Avahi---\n')
os.system('sudo systemctl start avahi-daemon')
