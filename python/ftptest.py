#!/bin/python3
# check for FTP TLS/SSL
# and anon login
import sys
import ftplib
if len(sys.argv) > 1:
        IP01 = sys.argv[1]
        print("[*] Testing: " + IP01)
else:
        print("[X] Usage: ftptest.py 10.0.0.0")
        exit()
USER01="anonymous"
PASS01="password"
try:
        ftps = ftplib.FTP_TLS(IP01)
        ftps.login(USER01,PASS01)
except:
        print(sys.exc_info()[1])
