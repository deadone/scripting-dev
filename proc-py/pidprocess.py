#!/usr/bin/python3
# Filename: pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *

process = LinuxProcList.proclist()
arrows = "|-------------->"
dashes = "----------------"
spaces = "                "
blacklist = []

for x in process:
    if str(x) not in blacklist:
        processchildren = LinuxProcList.children(x)
        if LinuxProcList.children(x) is not None:
            print(arrows,"PID: ",str(x).ljust(8, " "),LinuxProcList.getName(x).ljust(25, " "), end="")
            if LinuxProcList.cmdline(x) is not None:
                print("CMD:",LinuxProcList.cmdline(x))
            else:
                print()
            for y in LinuxProcList.children(x):
                blacklist.append(y)
                print(spaces + arrows,"PID: ", y.ljust(8," "),"Name:",LinuxProcList.getName(y).ljust(15, " "), end=" ")
                if LinuxProcList.children(y) is not None:
                    for z in LinuxProcList.children(y):
                        blacklist.append(z)
                        print("\n" + spaces + spaces + arrows, "PID: ", z.ljust(8, " "),"Name:",LinuxProcList.getName(y).ljust(15, " "), end="")
                        if LinuxProcList.cmdline(z) is not None:
                            print("CMD:", LinuxProcList.cmdline(z),end="")
                if LinuxProcList.cmdline(y) is not None:
                    print("CMD: ",LinuxProcList.cmdline(y))
                else:
                    print()
        else:
            print(arrows,"PID: ",str(x).ljust(8, " "), end="")
            if LinuxProcList.cmdline(x) is not None:
                print("CMD:",LinuxProcList.cmdline(x))
            else:
                print()