from base64 import *
from requests import get
from config import *
from json import *
from sys import argv, executable, exit

#check the config
try:
    config.check()
except:
    config.create()
modName = "selct mod"
r"""
    now that the config is validated, we can continue
"""
print("Interactive Setup Enviroment for PortalModTools v"+str(static.version()))
print("Current mod: "+modName)
print("\nWhat you want to do?")
print("1) Load Mod")
print("2) Create Mod")
print("3) Modify Mod")
print("4) Release Mod")
print("5) Quit")

