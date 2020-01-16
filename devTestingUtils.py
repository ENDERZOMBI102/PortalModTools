from base64 import *
from requests import get
from config import *
from json import *
from sys import argv, executable, exit
from zipfile import ZipFile
# checking if there's a config file, if not, we create one
try:
    config.check()
except:
    #config.create()
    pass
# checking if there's any arguments, if not, the program close
try:
    mode = argv[1]
except:
    print("No argumets inserted!")
    exit(1)


def compilee():
    print("compiling..")
    cmod = {"modName": "", "folderName": "", "light": False, "modZipData": ""}
    try:
        para = loads(argv[1])
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
        print("    checking zip file..")
        try:
            if not ".zip" in para["zipname"]:
                para["zipname"] = para["zipname"] + ".zip"
            with open(config.load("steamDir") + "\sourcemods\\" + config.load("modDirName") + "\\" + para["zipName"], "rb") as file:
                ZipFile(file, "r")
        except:
            print("    check failed! aborting..")
            print("\nCompilimg process aborted.\nReason: invalid zip")
            exit(1)
        print("    reading zip..")
        with open(config.load("steamDir") + "\sourcemods\\" + config.load("modDirName") + "\\" + para["zipName"], "rb") as file:
            cmod["modZipData"] = b64encode(file)
        cmod["modName"] = static.modName()
        cmod["folderName"] = config.load("modDirName")
        print("    saving file..")
        with open(static.modName()+".cmod", 'w', encoding="utf-8") as file:
                json.dump(cmod, file, indent=3)
        print("compiled successfully!")
    except Exception as e:
        print(e)
        print("compiling failed")
    finally:
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
# command: --help, diplay the help screen
if argv[0] == "--help":
    print("\nThis program is intended to be used by mod playtesters and developers.")
    print("aurgmets for this program are json-formatted.")
    print("Avaiable Commands:")
    print("     --help  display this screen.")
    print('     --setup {"steamDir": "", "modDirName": ""} setup the tools with the steam folder and/or mod name folder, usedef value on steamDir will use the default value')
    print('     compile {"zipName": "", "light":""} compiles the mod zip (that is inside the mod folder) to a modname.cmod file, modname is used to specify a mod, when light is true, this will only compile the files in the maps folder.')
    print('     install {"file": ""} install a mod.')
    print("\n\nTools By ENDERZOMBI102")
elif argv[0] == "--setup":
    pass
elif argv[0] == "compile":
    compilee()
elif argv[0] == "install":
    install()
        


def install():
    pass
