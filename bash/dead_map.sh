#!/bin/bash
# author: dead1
# script to enumerate hosts and
# scan and create folders with output

# network to scan
DEAD_NET="10.0.0.0"
DEAD_NOT="/24"
DEAD_NMAP="-sC -sV -oA"

# file management
DEAD_PROJECT="dead-scan"
DEAD_DIR="$PWD/$DEAD_PROJECT"
DEAD_HOSTS="${DEAD_DIR}/host-list"

# nmap ping scan & grep for IPs/hostnames
clear
echo ">>> Dead1's Nmap Automation <<<"
mkdir -p $DEAD_DIR
nmap -sn ${DEAD_NET}${DEAD_NOT} | grep -i "report for" | cut -b 22-50 > $DEAD_HOSTS
echo -e ">>> Hosts Found: <<<"
cat ${DEAD_HOSTS}
echo -e ""
echo -e "Scan these hosts? (y/n)"
read CONTINUE
echo -e ""

if [ "$CONTINUE" == "y" ]
then
	# nmap script scan on host(s)
	while IFS= read -r DEAD_HOST
	do
		DEAD_HOST=`echo $DEAD_HOST | cut -d " " -f 1`
		mkdir -p $DEAD_DIR/$DEAD_HOST
		nmap $DEAD_NMAP $DEAD_DIR/$DEAD_HOST/$DEAD_HOST $DEAD_HOST
	done < "$DEAD_HOSTS"
	echo -e "\n\n>>> Hosts Scanned <<<"
	cat ${DEAD_HOSTS}
	echo -e ""
fi
echo -e "\n.. Exitting\n"
