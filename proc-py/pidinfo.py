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
    dir_string = "/proc/" + pid + "/"
    if os.path.isdir(dir_string):
        process = linux_process(pid)
    else:
        print("Process Not Running.")
        exit()

    linux_proc_list.proc_list_plus()
    print()
    print("Process Viewer:")
    print("name:".rjust(12, " "), process.name().rjust(18, " "))
    print("state:".rjust(12, " "), process.state().rjust(18, " "))
    print("pid:".rjust(12, " "), process.pid().rjust(18, " "))
    print("ppid:".rjust(12, " "), process.ppid().rjust(18, " "))
    print("rss:".rjust(12, " "), hex(int(process.rss())).rjust(18, " "))
    print("rss_limit:".rjust(12, " "), hex(int(process.rss_limit())).rjust(18, " "))
    print("start_code:".rjust(12, " "), hex(int(process.start_code())).rjust(18, " "))
    print("end_code:".rjust(12, " "), hex(int(process.end_code())).rjust(18, " "))
    print("start_stack:".rjust(12, " "), hex(int(process.stack_start())).rjust(18, " "))
    print("start_data:".rjust(12, " "), hex(int(process.start_data())).rjust(18, " "))
    print("end_data:".rjust(12, " "), hex(int(process.end_data())).rjust(18, " "))
    print("start_brk:".rjust(12, " "), hex(int(process.start_brk())).rjust(18, " "))
    print("arg_start:".rjust(12, " "), hex(int(process.arg_start())).rjust(18, " "))
    print("arg_end:".rjust(12, " "), hex(int(process.arg_end())).rjust(18, " "))
    print("env_start:".rjust(12, " "), hex(int(process.env_start())).rjust(18, " "))
    print("env_end:".rjust(12, " "), hex(int(process.env_end())).rjust(18, " "))
    print()
    redo = str(input("Do you want to select another target? [y/n]: "))
    if redo == "y":
        pid = str(input("Please input the PID: "))
        print()
    else:
        print("Exiting.")
        quit()
