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
    pidStr = sys.argv[1]
else:
    pidStr = str(os.getpid())

loop = 1
while loop == 1:
    dirStr = "/proc/" + pidStr + "/"
    if os.path.isdir(dirStr):
        statStr = dirStr + "/stat"
        statusStr = dirStr + "/status"
        if os.path.isfile(statStr) and os.path.isfile(statusStr):
            process = LinuxProcess(pidStr)
        else:
            print('error.')
            exit()
    else:
        print("Process Not Running.")
        exit()
    LinuxProcList.proclistPlus()
    print()
    print("Process Viewer:")
    print("name:".rjust(12, " "), process.name().rjust(18, " "))
    print("state:".rjust(12, " "), process.state().rjust(18, " "))
    print("pid:".rjust(12, " "), process.pid().rjust(18, " "))
    print("ppid:".rjust(12, " "), process.ppid().rjust(18, " "))
    print("rss:".rjust(12, " "), process.rss().rjust(18, " "))
    print("rss_limit:".rjust(12, " "), process.rssLimit().rjust(18, " "))
    print("start_code:".rjust(12, " "), process.startCode().rjust(18, " "))
    print("end_code:".rjust(12, " "), process.endCode().rjust(18, " "))
    print("start_stack:".rjust(12, " "), process.stackStart().rjust(18, " "))
    print("start_data:".rjust(12, " "), process.startData().rjust(18, " "))
    print("end_data:".rjust(12, " "), process.endData().rjust(18, " "))
    print("start_brk:".rjust(12, " "), process.startBrk().rjust(18, " "))
    print("arg_start:".rjust(12, " "), process.argStart().rjust(18, " "))
    print("arg_end:".rjust(12, " "), process.argEnd().rjust(18, " "))
    print("env_start:".rjust(12, " "), process.envStart().rjust(18, " "))
    print("env_end:".rjust(12, " "), process.envEnd().rjust(18, " "))
    print()
    redo = str(input("Do you want to select another process? [y/n]: "))
    if redo == "y":
        pidStr = str(input("Please input the PID: "))
        print()
    else:
        print("Exiting.")
        quit()
