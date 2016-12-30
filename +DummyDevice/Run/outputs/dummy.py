import os, sys
import subprocess
try:
    print(subprocess.check_output('cat ' + os.path.dirname(os.path.realpath(sys.argv[0])) + '/../states/dummy', shell=True))
except:
    sys.exit(1)
