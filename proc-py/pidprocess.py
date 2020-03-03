#!/usr/bin/python3
# Filename: pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *

def recursiveChild(x, blacklist, repeat):
    arrows = "|-------------->"
    spaces = "                "
    if LinuxProcList.children(x) != None:
        repeat += 1
        for y in LinuxProcList.children(x):
            blacklist.append(y)
            print(spaces * repeat + arrows,str(y).ljust(8, " "), LinuxProcList.getName(y).ljust(20, " "), end="")
            if LinuxProcList.cmdline(y) != None:
                print(LinuxProcList.cmdline(y))
            else:
                print()
            recursiveChild(y, blacklist, repeat)
    return blacklist


process = LinuxProcList.proclist()
blacklist = []

for x in process:
    if str(x) not in blacklist:
        print("|-------------->", str(x).ljust(8, " "), LinuxProcList.getName(x).ljust(20, " "),color.nc, end="")
        if LinuxProcList.cmdline(x) != None:
            print(LinuxProcList.cmdline(x))
        else:
            print()
        blacklist = recursiveChild(x, blacklist, 0)
