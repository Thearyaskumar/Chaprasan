import os, socket, sys, time

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

print('Starting Flask Server...')
os.system('export FLASK_APP=flaskServer.py && flask run --host=0.0.0.0')
