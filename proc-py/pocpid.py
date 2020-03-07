#!/usr/bin/python3
# Filename: pocpid.py
# Author: dead1
# Details: proc

from deadlib import *

print(linux_proc_list.proc_list())
linux_proc_list.proc_list_plus()  ## added a better viewing option if a list wasnt desired.
print(linux_proc_list.cmd_line(4254))
print(linux_proc_list.children(2))
