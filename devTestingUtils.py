from base65536 import encode
from requests import get
from config import *
from json import *
from sys import argv, executable, exit
from zipfile import ZipFile
# checking if there's a config file, if not, we create one
try:
    config.check()
except Exception as e:
    print(e)
    #config.create()
    pass
# checking if there's any arguments, if not, the program close
try:
    mode = argv[1]
except:
    print("No argumets inserted!")
    #exit(1)
    argv.append("compile")
    argv.append("zipName=pft.zip")
# strange workaround command line limitations


def compilee():
    # stating to compile the mod
    print("compiling..")
    # create cmod default dict
    cmod = {"modName": "", "folderName": "", "light": False, "modZipData": ""}
    # a try for the aurgment part
    try:
        # loads the arguments and check them
        print("    checking parameters..")
        para = {"light": False}
        # parse the parameters
        for i in argv:
            if "zipName" in i:
                print("    found parameter: zipName")
                para["zipName"] = i.replace("zipName=", "")
                print(para["zipName"])
            if "light" in i:
                print("    found parameter: light")
                para["light"] = i.replace("light=", "")
        # check if there's the zipName parameter, if not exit
        if not para["zipName"]:
            print("you need to specify a zip file!")
            exit(1)
        if para["light"] in [True, False, "true", "false"]:# if there's a light parameter load it
            if para["light"] in [False, "false"]:
                cmod["light"] = False
            elif para["light"] in [True, "true"]:
                cmod["light"] = True
            else:# the light parameter wasn't a boolean value
                print("error during handling of the light parameter, expected True (or true) or False (or false)")
                exit(1)# bellow: catch song!
    except Exception as e:# catch the error!
        print("compiling failed")# do a stdout
        print(e)  # print it out
        exit(1)# and then when done exit from this code
    #zip file checking part
    print("    checking zip file..")
    try:
        if not ".zip" in para["zipName"]:# adds the extension if there isn't
            para["zipName"] = para["zipName"] + ".zip"
        with open(config.load("steamDir") + "\steamapps\sourcemods\\" + config.load("modDirName") + "\\" + para["zipName"], "rb") as file:
            ZipFile(file)# check if it exist and if is a zip file
    except Exception as e:
        print("    check failed! aborting..")
        print("Compiling process aborted.\nReason: invalid or inesistent zip file")
        print(e)
        exit(1)
    # zip encoding part
    print("    reading zip..")
    try:
        with open(config.load("steamDir") + "\steamapps\sourcemods\\" + config.load("modDirName") + "\\" + para["zipName"], "rb") as file:
            cmod["modZipData"] = str(encode(file.read()))# open the zip file and encode it in base64
        print("    loading mod info..")
        cmod["modName"] = static.modName()# load the mod name from the config and put it in the file
        cmod["folderName"] = config.load("modDirName")# loads the dir name and put it in the file
    except Exception as e:
        print("compiling failed")
        print(e)
        exit(1)
    try:
        print("    saving file..")
        with open(static.modName()+".cmod", 'w', encoding="utf-8") as file:
                dump(cmod, file, indent=3)# save the file
        print("compiled successfully!")
    except Exception as e:
        print("compiling failed")
        print(e)
        exit(1)
    exit(0)# normal program exit


#quick check if we are on a compiled version or not
if "py" in executable:
    print("executed from: python source file, executed on "+static.osType())
    compiled = False
else:
    print("executed from: compiled exec file, executed on "+static.osType())
    compiled = True
# program start
print(static.name() + " v." + static.version() + " - DevTesting Releases Tool")# first informations
# command "processor"
# command: --help, diplay the help screen
if argv[1] == "--help":
    print("\nThis program is intended to be used by mod playtesters and developers.")
    print("parameters values can be putted after the =, the args can't contain spaces.")
    print("Avaiable Commands:")
    print("     --help  display this screen.")
    print('     compile zipName= light= compiles the mod zip (that is inside the mod folder) to a modname.cmod file, when light is true, this will only compile the files in the maps folder.')
    print('     install {"file":""} install a mod.')
    print("\n\nTools By ENDERZOMBI102")
elif argv[1] == "--setup":
    pass
elif argv[1] == "compile":
    compilee()
elif argv[1] == "install":
    install()
else:
    print("Undefined error!")
        


def install():
    pass
