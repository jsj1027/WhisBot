import os
import sys
def fix(topfile):
    currentDir = ""
    while currentDir != f'{topfile}':
        pathSplit = os.getcwd().split("\\")
        pathLen = len(pathSplit)
        currentDir = pathSplit[pathLen-1]
        os.chdir("..")
    os.chdir(f"{topfile}")
    
def back(normal):
    os.chdir(f"{normal}")

sys.path.append(os.getcwd())