#!/usr/bin/python3
# Filename: pocpid.py
# Author: dead1
# Details: proc

from deadlib import *
# proof of concept use of classes from deadlib
print(linux_proc_list.proc_list())
linux_proc_list.proc_list_plus()  ## added a better viewing option if a list wasnt desired.
print(linux_proc_list.cmd_line(2))
print(linux_proc_list.children(2))
