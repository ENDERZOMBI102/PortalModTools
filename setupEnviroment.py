from base64 import *
from requests import get
from config import *
from json import *
from sys import argv, executable, exit

class main:
    def __init__(self):
        #check the config
        try:
            config.check()
        except:
            config.create()
        # declare global variables
        self.modName = "select a mod"
        self.exit = False
        self.versionControl = "off"
        self.currentMenu = 0
        r"""
            now that the config is validated, we can continue
        """
        # lets open the main menu
        while not self.exit:
            if self.currentMenu == 0:
                self.mainMenu0()
            elif self.currentMenu == 1:
                self.loadModMenu0()
            elif self.currentMenu == 2:
                self.createModMenu0()
            elif self.currentMenu == 3:
                self.modifyModMenu0()
            elif self.currentMenu == 4:
                self.releaseModMenu0()



    def mainMenu0(self):
        print("Interactive Setup Enviroment for PortalModTools v" + str(static.version()))
        print("Current Mod: " + self.modName + ", Version Control: " + self.versionControl)
        print("\nWhat you want to do?")
        print("1) Load Mod")
        print("2) Create Mod")
        print("3) Modify Mod")
        print("4) Release Mod")
        print("5) Quit")
        choice = input()
        # check user input
        while not choice in (1, 2, 3, 4, 5)
            choice = input()
        if choice == 1:
            self.currentMenu = 1
        elif choice == 2:
            self.currentMenu = 2
        elif choice == 3:
            self.currentMenu = 3
        elif choice == 4:
            self.currentMenu = 4
        elif choice == 5:
            if input("\nAre you sure that you want to quit?") in ("yes", "y", "s", "si", 1):
                # with this True the loop is broken
                self.exit = True
                # this is only for safety
                self.currentMenu = 10
                # return to main function
                return
        
    def loadModMenu0(self):
        pass
    
    def createModMenu0(self):
        modName = input("Insert Mod Name")
        dirName = input("Insert mod dir name")
        x = 0
        while True:
            authors[x] = input("Insert author " + str(x) + ", s to stop")
            if author[x] == "s":
                author[x] == None
                break
            x+=1
        static.createMod(modname, dirName, authors)


