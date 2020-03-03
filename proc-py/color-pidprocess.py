#!/usr/bin/python3
# Filename: color-pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *

def recursiveChild(x, blacklist, repeat):
    arrows = "\__________"
    spaces = "           "
    col = ""
    if LinuxProcList.children(x) != None:
        repeat += 1
        col = colrep(repeat)
        for y in LinuxProcList.children(x):
            blacklist.append(y)
            print(col + spaces * repeat + arrows,str(y).ljust(8, " "), LinuxProcList.getName(y).ljust(20, " "), end="")
            if LinuxProcList.cmdline(y) != None:
                print(LinuxProcList.cmdline(y) + color.nc)
            else:
                print(color.nc)
            blacklist.append(recursiveChild(y, blacklist, repeat))
    return blacklist


process = LinuxProcList.proclist()
blacklist = []

print("Dead1's PID Process Tree:")
for x in process:
    repeat = 0
    col = colrep(repeat)
    if str(x) not in blacklist:
        blacklist.append(x)
        print(col + "\__________", str(x).ljust(8, " "), LinuxProcList.getName(x).ljust(20, " "), end="")
        if LinuxProcList.cmdline(x) != None:
            print(LinuxProcList.cmdline(x) + color.nc)
        else:
            print(color.nc)
        blacklist.append(recursiveChild(x, blacklist, repeat))
