import srctools as src
import os
import sys
import subprocess
import glob
import pathlib

vvis = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/bin/vvis.exe'
vrad = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/bin/vrad.exe'
vbsp = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/bin/vbsp.exe'
post = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/postcompiler/postcompiler.exe'

gamedir = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/portal2'

bspdir = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/portal2/maps'
bspdirdlc3 = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/portal2_dlc3/maps'

path = r'H:/Antonios stuff/program files/Steam/SteamApps/common/Portal 2/sdk_content/maps/PFT'

ptffolder = r'H:/Antonios stuff/program files/Steam/SteamApps/sourcemods/Portal Forever Testing (release)/'

# remove all .dem files (?)
subprocess.run(gamedir + '/deldemos.bat')

move = ''  # so the while loop has a variable to check
while move not in ['y', 'n']:
    move = input('move maps to release folder? (y/n)')  # ask if want to move files
print('finding maps...')
print(f'found {len(glob.glob(path+"/*.vmf"))} maps!')
for map in glob.glob(bspdir + '/*.vmf'):
    if "_old.vmf" in map:
        # if has _old in the name do nothing
        continue
    bsppath = map.replace('.vmf', '.bsp')  # the path to map's bsp file
    pathobj = pathlib.Path(map)  # obj for later use
    if pathlib.Path(bsppath).exists():
        os.remove(bsppath)  # if the .bsp exist delete it
    print(f'compiling map: {pathobj.name}')
    # run VBSP
    print(subprocess.run(executable=vbsp, args=f'-game "{gamedir}" "{map}"').stdout)
    # run srctools's postcompiler
    print(subprocess.run(executable=post, args=f'"{bsppath}"').stdout)
    # run VVIS
    print(subprocess.run(executable=vvis, args=f'-game "{gamedir}" "{bsppath}"').stdout)
    # run VRAD
    print(subprocess.run(executable=vrad, args=f'-game "{gamedir}" -both -final -staticproplighting -staticproppolys -textureshadows "{bsppath}"').stdout)
    print(f'moving {pathobj.name}..')
    if move == 'y':
        with pathlib.Path(bsppath).read_bytes() as bspbytes:
            pathlib.Path(ptffolder+f'maps/{pathobj.name.replace(".vmf", ".bsp")}').write_bytes(bspbytes)
        os.remove(bsppath)
print('finished compiling!')
