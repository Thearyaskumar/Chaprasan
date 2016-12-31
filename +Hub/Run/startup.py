import os, sys, subprocess, time

print("Checking for other hub")
myips = subprocess.check_output('hostname -I', shell=True).split()
if not any('hub.local' in subprocess.check_output('avahi-resolve-address ' + ip, shell=True) for ip in myips):
    print('Found another hub')
    sys.exit(1)
print('No other hub found')

print('Starting Flask Server')
os.system('export FLASK_APP=flaskServer.py && flask run --host=0.0.0.0')
