import os
import sys
import subprocess

#Check for root:
if os.getuid() != 0:
    print('Script requires root.')
    sys.exit()

dirs = [d for d in os.listdir('.') if (os.path.isdir(os.path.join('.', d)) and os.path.basename(os.path.join('.', d)).startswith("+"))]

print("Welcome to the install script!\n")
print("Here are all valid devices:")
for dev in range(0, len(dirs)):
	print(str(dev+1) + ") " + str(dirs[dev])[1:])

def pickDevice():
	user = input("\nEnter a number from 1 to " + str(len(dirs)) + ". (-1 to quit): ")
	if(int(user) == -1):
		print("Quitting")
		sys.exit()
	elif(int(user) < 1 or int(user) > len(dirs)):
		print("Invalid Input:")
		return pickDevice()
	else:
		return dirs[int(user)-1]

chosenDir = pickDevice()
print("\nDevice \"" + str(chosenDir)[1:] + "\" chosen.")

subprocess.call(["python", "master.py"], cwd=os.path.abspath(os.path.join('.', chosenDir, "Setup")))
