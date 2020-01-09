from base64 import *
from requests import get
from config import *
from sys import argv, executable, exit
# checking if there's a config file, if not, we create one
try:
    config.check()
except:
    config.create()
# checking if there's any arguments, if not, the program close
try:
    mode = argv[1]
except:
    print("No argumets inserted!")
    exit(1)
#quick check if we are on a compiled version or not
if "py" in executable:
    print("executed from: python source file, executed on "+static.osType())
    compiled = False
else:
    print("executed from: compiled exec file, executed on "+static.osType())
    compiled = True
# program start
print(static.name() + " v." + static.version() + " - DevTesting Releases Tool")# fist informations
if argv[0] == "devTestingUtils.py": # this will delete the name of the file from the list
    argv.remove("devTestingUtils.py")
# command "processor"
if argv[0] == "--help":
    print("\nThis program is intended to be used by mod playtesters and developers.")
    print("aurgmets for this program are json-formatted.")
    print("Avaiable Commands:")
    print("     --help display this screen.")
    print('     --setup {"steamDir": "", "modDirName": ""} setup the tools with the steam folder and/or mod name folder.')
    print('     compile {"modname": "", "light":""}compiles the mod to a modname.cmod file, modname is used to specify a mod, light is used to compile only the files in the maps folder.')
    print('     install {"file": ""} install a mod.')
    print("     ")
