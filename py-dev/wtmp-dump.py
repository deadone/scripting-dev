#!/usr/bin/python3
# Filename: wtmp-dump.py
# Author: dead1
# Details: WTMP Output to quickly see logins

import subprocess

tempstring = ""
return_string = subprocess.run(['last', '-f', '/var/log/wtmp'], stdout=subprocess.PIPE).stdout.decode('utf-8')
return_string = return_string.split('\n')

new_list = []

for x in range(0, len(return_string)):
    if 'reboot' in return_string[x]:
        continue
    elif 'wtmp' in return_string[x]:
        continue
    else:
        new_list.append(return_string[x])

print("Dead1's WTMP Dump\nDate:\t   Time:   Until: Who:\t\tFrom:")
for x in range(0, len(new_list)):
    print(new_list[x][39:64],new_list[x][0:9],new_list[x][22:39])
