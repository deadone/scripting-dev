#!/usr/bin/python3
# Filename: pidinfo.py
# Author: dead1
# Details: proc

################################
## Usage: python3 pidinfo.py
##   Or:  python3 pidinfo.py <PID>
################################

import os
import sys

from deadlib import *

if len(sys.argv) == 2:
    pid = sys.argv[1]
else:
    pid = str(os.getpid())

loop = 1
while loop == 1:
    linux_proc_list.proc_list_plus()
    linux_proc_list.process_viewer(pid)
    redo = str(input("\nDo you want to select another process? [y/n]: "))
    if redo == "y":
        pid = str(input("Please input the PID: "))
        print()
    else:
        print("Exiting.")
        quit()
