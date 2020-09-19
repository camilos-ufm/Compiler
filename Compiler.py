# imports
import sys

if (len(sys.argv) == 3):
    print("file: " + sys.argv[0])
    print("[option]: " + sys.argv[1])
    print("<filename>: " + sys.argv[2])
elif (len(sys.argv) == 2):
    print("Show Help.")
else:
    print("'option' parameter missing.")
