import os
import subprocess

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

print('\n---Copying Runfiles---\n')
os.system('rm -Rf /srv/chaprasan')
os.system('mkdir /srv/chaprasan && cp ../Run/* /srv/chaprasan/ && chmod +x /srv/chaprasan/startup.sh && chown root /srv/chaprasan')

print('\n---Installing Service---\n')

print('Copying the service file...')
os.system('sudo cp ./chaprasan.service /etc/systemd/system/ && sudo chmod 0644 /etc/systemd/system/chaprasan.service')

print('Enabling in systemd...')
os.system('sudo systemctl enable chaprasan.service')

print('\n---Restarting Service---\n')
os.system('sudo systemctl restart chaprasan.service')
