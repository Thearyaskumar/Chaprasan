import os
dirs = [d for d in os.listdir('.') if (os.path.isdir(os.path.join('.', d)) and os.path.basename(os.path.join('.', d)).startswith("+"))]
print str(dirs)
