from base64 import *
from requests import get
from config import *
from json import *
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
    print('     --setup {"steamDir": "", "modDirName": ""} setup the tools with the steam folder and/or mod name folder, usedef value on steamDir will use the default value')
    print('     compile {"zipName": "", "light":""} compiles the mod zip (that is inside the mod folder) to a modname.cmod file, modname is used to specify a mod, when light is true, this will only compile the files in the maps folder.')
    print('     install {"file": ""} install a mod.')
    print("\n\nTools By ENDERZOMBI102")
elif argv[0] == "--setup":
    try:
        para = loads(argv[1])
    except:
        print("no parameters given.")
        exit(1)
    try:
        if para["steamDir"] == "usedef":
            print("Using default windows path for steamDir...")
            config.save("C:\Program Files (x86)\Steam\\","steamDir")
        else:
            config.save(para["steamDir"], "steamDir")
    except:
        if static.steamDir() == "":
            print("no steam dir given, using windows defaults....")
            config.save("C:\Program Files (x86)\Steam\\","steamDir")
    try:
        config.save(para["modDirName"], "modDirName")
    except:
        if config.load("modDirName") == "":
            print("no mod dir given, leaving blank")
elif argv[0] == "compile":
    print("compiling..")
    cmod = {"modName": "", "folderName": "", "light": False, "modZipData": ""}
    try:
        para = argv[1]
        print("    checking parameters..")
        if not para["zipName"]:
            print("you need to specify a zip file!")
            exit(1)
        if para["light"]:
            if para["light"] in [False, "false"]:
                cmod["light"] = False
            elif para["light"] in [True, "true"]:
                cmod["light"] = True
            else:
                print("error during handling of the light parameter, expected True (or true) or False (or false)")
                exit(1)
        print("    reading zip..")
        with open(config.load("steamDir") + "\steamapps\\" + config.load("modDirName") + "\\" + para["zipName"]) as file:
            cmod["modZipData"] = b64encode(file)
        cmod["modName"] = static.modName()
        cmod["folderName"] = config.load("modDirName")
        print("    saving file..")
        with open(static.modName()+".cmod", 'w', encoding="utf-8") as file:
                json.dump(cmod, file, indent=3)
        print("compiled successfully!")
    except:
        print("compiling failed")
    finally:
        exit(1)
elif argv[0] == "install":
        
        