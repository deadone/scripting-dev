#!/bin/python3
# author: dead1
# quickly generate base64
# encoded combination wordlists

import base64

username = "admin"
inputf = "/opt/wordlists/top1k.txt"
outputf = "base64-out.txt"

pass_file = open(inputf,'r')

pass_raw = pass_file.readlines()
pass_list = []

for password in pass_raw:
	pass_list.append(password.strip())

for x in range(0,len(pass_list)):
	data = username + ":" + pass_list[x]
	encodedBytes = base64.b64encode(data.encode("utf-8"))
	encodedStr = str(encodedBytes, "utf-8")
	pass_list[x] = encodedStr

with open(outputf, 'w') as out_file:
	for item in pass_list:
		out_file.write("%s\n" % item)

print("[*] Dead1's Quick Base64 Combo Encoder")
print("[*] Username used: " + username)
print("[*] Input wordlist: " + inputf)
print("[*] Base64 Words Generated: " + str(len(pass_list)))
print("[*] File saved as: " + outputf)

pass_file.close()
out_file.close()
