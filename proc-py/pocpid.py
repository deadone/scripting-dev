#!/usr/bin/python3
# Filename: pocpid.py
# Author: dead1
# Details: proc

from deadlib import *

print(LinuxProcList.proclist())
LinuxProcList.proclistPlus()  ## added a better viewing option if a list wasnt desired.
print(LinuxProcList.cmdline(1))
print(LinuxProcList.children(2))
