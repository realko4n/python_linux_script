import os
import sys

if (os.path.isfile(sys.argv[1])):
    print(sys.argv[1], "- file")
elif (os.path.isdir(sys.argv[1])):
    print(sys.argv[1], "- dir")
else:
    print(sys.argv[1], "- not exist")