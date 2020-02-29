#!/usr/bin/python3
# Filename: pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *

class color:
    blue = '\033[94m' # blue
    green = '\033[92m' # pale green
    yellow = '\033[93m' # yellow
    red = '\033[91m' # red
    bold = '\033[1m' # bold
    uline = '\033[4m' #underline
    nc ='\x1b[0m' # No Color

process = LinuxProcList.proclist()
arrows = "|-------------->"
dashes = "----------------"
spaces = "                "
blacklist = []

for x in process:
    if str(x) not in blacklist:
        processchildren = LinuxProcList.children(x)
        if LinuxProcList.children(x) is not None:
            print(color.red + color.bold + arrows,str(x).ljust(8, " "),LinuxProcList.getName(x).ljust(20, " "),color.nc, end="")
            if LinuxProcList.cmdline(x) is not None:
                print(LinuxProcList.cmdline(x))
            else:
                print()
            for y in LinuxProcList.children(x):
                blacklist.append(y)
                print(color.blue + color.bold + spaces + arrows, y.ljust(8," "),LinuxProcList.getName(y).ljust(20, " "),color.nc, end=" ")
                if LinuxProcList.children(y) is not None:
                    for z in LinuxProcList.children(y):
                        blacklist.append(z)
                        print("\n" + color.bold + color.green + spaces + spaces + arrows,z.ljust(8, " "),LinuxProcList.getName(y).ljust(20, " "),color.nc, end="")
                        if LinuxProcList.cmdline(z) is not None:
                            print(LinuxProcList.cmdline(z),end="")
                if LinuxProcList.cmdline(y) is not None:
                    print(LinuxProcList.cmdline(y))
                else:
                    print()
        else:
            print(color.red + color.bold + arrows,str(x).ljust(8, " "),color.nc, end="")
            if LinuxProcList.cmdline(x) is not None:
                print(LinuxProcList.cmdline(x))
            else:
                print()
