#!/usr/bin/python3
# Filename: pocpid.py
# Author: dead1
# Details: proc

from deadlib import *
# proof of concept use of classes from deadlib
print(linux_proc.proc_list())
linux_proc.proc_list_plus()  # added a better viewing option if a list wasnt desired.
print(linux_proc.cmd_line(4254))
print(linux_proc.children(2))
