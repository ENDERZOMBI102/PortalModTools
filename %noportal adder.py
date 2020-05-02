from sys import argv
from glob import glob
import PIL

if len(argv) < 2:
    print("this utility add %noportal 1 value to a .vmt")
    print(f'usage: {argv[0]} -f folderpath, to use on all vtf/vmt in a folder')
    print(f'usage: {argv[0]} filepath. to use on a single file')
    quit()

if "-f" in argv:
    folder = argv[argv.index("-f") + 1]
    for path in glob(folder+'/*.vmt'):
        single(path)
else: single(argv[1])

def single(path: str):
    with open(path, "r") as file:
        data = file.read()
    data = data.replace('}', '    "%noportal" "1"\n}')
    with open(path, 'w') as file:
        file.write(data)

