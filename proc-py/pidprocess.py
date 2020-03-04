#!/usr/bin/python3
# Filename: pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *

def recursiveChild(x, blacklist, repeat):
    arrows = "\_________ "
    spaces = "           "
    col = ""
    if LinuxProcList.children(x) != None:
        repeat += 1
        for y in LinuxProcList.children(x):
            blacklist.append(y)
            print(spaces * repeat + arrows + str(y).ljust(8, " ") + LinuxProcList.getName(y).ljust(20, " "), end="")
            if LinuxProcList.cmdline(y) != None:
                print(LinuxProcList.cmdline(y))
            else:
                print()
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
        print("\__________" + str(x).ljust(8, " ") + LinuxProcList.getName(x).ljust(20, " "), end="")
        if LinuxProcList.cmdline(x) != None:
            print(LinuxProcList.cmdline(x))
        else:
            print()
        blacklist.append(recursiveChild(x, blacklist, repeat))
        print()
