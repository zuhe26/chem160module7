import sys
import os
from os import path
filename=input("Enter the name of the file: ")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file=open(filename,"r")
while 1:
    line=file.readline()
    print(line,end="")
    if line=="":
        break
