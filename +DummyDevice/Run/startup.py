import os, socket, sys, time, requests, subprocess

print('\nDummyDevice Starting...')

def checkForHub(val):
    if val > 10:
	print("Hub not found. Aborting...")
        sys.exit(1)
    try:
        socket.gethostbyname('hub.local')
        print("Hub found!")
    except socket.error:
        print("Hub not found. Retrying in 10 seconds...")
	time.sleep(10)
        checkForHub(val+1)

checkForHub(0)

my_location = subprocess.check_output('avahi-resolve-address ' + subprocess.check_output('hostname -I', shell=True).split()[0], shell=True).split()[1]

print('Connecting to Hub...')
try:
    r = requests.post("http://hub.local:5000/addDevice", data={'location': my_location, 'inputs': str(os.listdir("./inputs")),'outputs': str(os.listdir("./outputs"))})
except Exception, e:
    print('ERROR:' + str(e))
    sys.exit(1)
if r.status_code == 200:
    print('Starting Flask Server...')
elif r.status_code == 406:
    print('Already connected to Hub!') #UPDATE INPUTS AND OUTPUTS HERE
else:
    print('Some error occored: ' + str(r.status_code))
    sys.exit(1)

os.system('export FLASK_APP=flaskServer.py && flask run --host=0.0.0.0')
