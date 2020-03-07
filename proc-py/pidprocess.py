#!/usr/bin/python3
# Filename: pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *


def recursive_child(x, blacklist, repeat):
    arrows = "\_________ "
    spaces = "           "
    col = ""
    if linux_proc.children(x) != None:
        repeat += 1
        for y in linux_proc.children(x):
            blacklist.append(y)
            print(spaces * repeat + arrows + str(y).ljust(8, " ") + linux_proc.get_name(y).ljust(20, " "), end="")
            if linux_proc.cmd_line(y) != None:
                print(linux_proc.cmd_line(y))
            else:
                print()
            blacklist.append(recursive_child(y, blacklist, repeat))
    return blacklist


process = linux_proc.proc_list()
blacklist = []

print("Dead1's PID Process Tree:")
for x in process:
    repeat = 0
    if str(x) not in blacklist:
        blacklist.append(x)
        print("\__________" + str(x).ljust(8, " ") + linux_proc.get_name(x).ljust(20, " "), end="")
        if linux_proc.cmd_line(x) != None:
            print(linux_proc.cmd_line(x))
        else:
            print()
        blacklist.append(recursive_child(x, blacklist, repeat))
        print()
