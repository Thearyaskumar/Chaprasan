import sys
import os
try:
    os.system('sudo rm ' + os.path.dirname(os.path.realpath(sys.argv[0])) + '/../states/dummy')
except:
    pass
os.system('touch ' + os.path.dirname(os.path.realpath(sys.argv[0])) + '/../states/dummy')
with open(os.path.dirname(os.path.realpath(sys.argv[0])) + "/../states/dummy", "w") as text_file:
    text_file.write(sys.argv[1])

sys.exit(0)
