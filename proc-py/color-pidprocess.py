#!/usr/bin/python3
# Filename: color-pidprocess.py
# Author: dead1
# Details: proc

from deadlib import *


## proof I could have made this recursively, I just wanted to use colors.
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
arrows = "|-------------->"
spaces = "                "
blacklist = []
parent = color.red + color.bold + arrows
first = color.blue + color.bold + spaces + arrows
second = color.lightblue + color.bold + (2 * spaces) + arrows
third = color.lightgreen + color.bold + (3 * spaces) + arrows
fourth = color.cyan + color.bold + (4 * spaces) + arrows
fifth = color.yellow + color.bold + (5 * spaces) + arrows
sixth = color.pink + color.bold + (6 * spaces) + arrows
seventh = color.lightred + color.bold + (7 * spaces) + arrows

for x in process:
    if str(x) not in blacklist:
        print(parent, str(x).ljust(8, " "), LinuxProcList.getName(x).ljust(20, " "), end="")
        if LinuxProcList.cmdline(x) != None:
            print(color.red, LinuxProcList.cmdline(x), color.nc)
        else:
            print()
        if LinuxProcList.children(x) != None:
            for y in LinuxProcList.children(x):
                blacklist.append(y)
                print(first, str(y).ljust(8, " "), LinuxProcList.getName(y).ljust(20, " "), end="")
                if LinuxProcList.cmdline(y) != None:
                    print(color.blue, LinuxProcList.cmdline(y), color.nc)
                else:
                    print()
                if LinuxProcList.children(y) != None:
                    for z in LinuxProcList.children(y):
                        blacklist.append(z)
                        print(second, str(z).ljust(8, " "), LinuxProcList.getName(z).ljust(20, " "), end="")
                        if LinuxProcList.cmdline(z) != None:
                            print(color.lightblue, LinuxProcList.cmdline(z), color.nc)
                        else:
                            print()
                        if LinuxProcList.children(z) != None:
                            for zz in LinuxProcList.children(z):
                                blacklist.append(zz)
                                print(third, str(zz).ljust(8, " "), LinuxProcList.getName(zz).ljust(20, " "), end="")
                                if LinuxProcList.cmdline(zz) != None:
                                    print(color.lightgreen, LinuxProcList.cmdline(zz), color.nc)
                                else:
                                    print()
                            if LinuxProcList.children(zz) != None:
                                for xx in LinuxProcList.children(zz):
                                    blacklist.append(xx)
                                    print(fourth, str(xx).ljust(8, " "), LinuxProcList.getName(xx).ljust(20, " "),
                                          end="")
                                    if LinuxProcList.cmdline(xx) != None:
                                        print(color.cyan, LinuxProcList.cmdline(xx), color.nc)
                                    else:
                                        print()
                                    if LinuxProcList.children(xx) != None:
                                        for qq in LinuxProcList.children(xx):
                                            blacklist.append(qq)
                                            print(fifth, str(qq).ljust(8, " "),
                                                  LinuxProcList.getName(qq).ljust(20, " "), end="")
                                            if LinuxProcList.cmdline(qq) != None:
                                                print(color.yellow, LinuxProcList.cmdline(qq), color.nc)
                                            else:
                                                print()
                                            if LinuxProcList.children(qq) != None:
                                                for tt in LinuxProcList.children(qq):
                                                    blacklist.append(tt)
                                                    print(sixth, str(tt).ljust(8, " "),
                                                          LinuxProcList.getName(tt).ljust(20, " "), end="")
                                                    if LinuxProcList.cmdline(tt) != None:
                                                        print(color.pink, LinuxProcList.cmdline(tt), color.nc)
                                                    else:
                                                        print()
                                                    if LinuxProcList.children(tt) != None:
                                                        for pp in LinuxProcList.children(tt):
                                                            blacklist.append(pp)
                                                            print(sixth, str(pp).ljust(8, " "),
                                                                  LinuxProcList.getName(pp).ljust(20, " "), end="")
                                                            if LinuxProcList.cmdline(pp) != None:
                                                                print(color.lightred, LinuxProcList.cmdline(pp),
                                                                      color.nc)
                                                            else:
                                                                print()
