from base64 import *
from requests import get
from config import *
from json import *
from sys import argv, executable, exit



# initialize the SE module
print("initializing setup.", end="")

print(".", end="")
if argv[1]:
      if argv[1] in ["--tutorial", "--help"]:
            pass            
      else:
            print("g")

