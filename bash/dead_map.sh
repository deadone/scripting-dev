#!/bin/bash
# author: dead1
# script to enumerate hosts and
# scan and create folders with output

# nmap settings
DEAD_NMAP="-sC -sV -oA"

# file management
DEAD_PROJECT="dead-scan"
DEAD_DIR="$PWD/$DEAD_PROJECT"
DEAD_HOSTS="${DEAD_DIR}/host-list"

# nmap ping scan & grep for IPs/hostnames
clear
echo -e ">>> Dead1's Nmap Automation <<<\n"
echo -e ">>> Networks you are on:"
ifconfig | grep -i "inet " | cut -d " " -f 10
echo -e "\n>>> Select Host/Network: (eg: 10.0.0.1)"
read DEAD_NET
echo -e "\n>>> Subnet: (eg: 24)"
read DEAD_NOT
echo -e ""
mkdir -p $DEAD_DIR
nmap -sn ${DEAD_NET}/${DEAD_NOT} | grep -i "report for" | cut -b 22-50 > $DEAD_HOSTS
echo -e ">>> Hosts Found:"
cat ${DEAD_HOSTS}
echo -e ""
echo -e ">>> How to Proceed:\n1 - Scan One Host\n2 - Scan All Hosts\n3 - Exit"
echo -e "\n>>> Enter Choice: (eg: 1)"
PROCEED=3
read PROCEED
echo -e ""

if [ "$PROCEED" == "1" ]
then
	rm -rf $DEAD_DIR
	echo -e ">>> Enter Host:"	
	read DEAD_HOST
	echo -e ""
	mkdir -p dead_output
	nmap $DEAD_NMAP dead_output/$DEAD_HOST $DEAD_HOST
	echo -e "\n>>> Output Saved:\n$PWD/dead_output/$DEAD_HOST.nmap\n"
	exit	
fi

if [ "$PROCEED" == "2" ]
then
	# nmap script scan on host(s)
	while IFS= read -r DEAD_HOST
	do
		DEAD_HOST=`echo $DEAD_HOST | cut -d " " -f 1`
		mkdir -p $DEAD_DIR/$DEAD_HOST
		nmap $DEAD_NMAP $DEAD_DIR/$DEAD_HOST/$DEAD_HOST $DEAD_HOST
	done < "$DEAD_HOSTS"
	echo -e "\n\n>>> Hosts Scanned:"
	cat ${DEAD_HOSTS}
	echo -e "\n>>> Output Files\n>>> Located at ${DEAD_DIR}"
	ls -la $DEAD_DIR
	exit
fi
echo -e ".. Exiting\n"
exit
