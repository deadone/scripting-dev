#!/bin/bash
# author: dead1
# script to enumerate hosts and
# scan and create folders with output

# nmap settings
DEAD_NMAP="-sC -sV -oA"

# file management
DEAD_PROJECT="oscp" 		# engagement name
DEAD_DIR="$PWD/$DEAD_PROJECT"
DEAD_HOSTS="${DEAD_DIR}/host-list"

# colours
CL8='\033[1;31m' #light red
NC='\033[0m' #No color
COL1="${CL8}>>>${NC}"

# nmap ping scan & grep for IPs/hostnames
clear
echo -e "${COL1} Dead1's Nmap Automation ${CL8}<<<${NC}\n"
echo -e "${COL1} Networks/Interfaces You Are On"
ifconfig | grep -i "inet " | cut -d " " -f 10
echo -e "\n${COL1} Select Host/Network (eg: 10.0.0.1)"
read DEAD_NET
echo -e "\n${COL1} Subnet Cidr (eg: 24)"
read DEAD_NOT
echo -e "\n${COL1} Running Ping Scan ... (Please Wait)"
echo -e ""
mkdir -p $DEAD_DIR
nmap -sn ${DEAD_NET}/${DEAD_NOT} | grep -i "report for" | cut -b 22-50 > $DEAD_HOSTS
echo -e "${COL1} Found Hosts"
cat ${DEAD_HOSTS}
echo -e ""
echo -e "${COL1} Proceed\n1 - Scan One Host\n2 - Scan All Hosts\n3 - Exit"
echo -e "\n${COL1} Enter Choice (eg: 1)"
PROCEED=3
read PROCEED
echo -e ""

if [ "$PROCEED" == "1" ]
then
	rm -rf $DEAD_DIR
	echo -e "${COL1} Enter Host"	
	read DEAD_HOST
	echo -e ""
	mkdir -p $DEAD_PROJECT
	nmap $DEAD_NMAP $DEAD_PROJECT/$DEAD_HOST $DEAD_HOST
	echo -e "\n${COL1} Output Saved\n$DEAD_DIR/$DEAD_HOST.nmap\n"
	exit	
fi

if [ "$PROCEED" == "2" ]
then
	# nmap script scan on host(s)
	echo -e "${COL1} Scanning ALL hosts ... (Please Wait)"
	while IFS= read -r DEAD_HOST
	do
		DEAD_HOST=`echo $DEAD_HOST | cut -d " " -f 1`
		echo -e "${COL1} Scanning host ${DEAD_HOST} ..."
		mkdir -p $DEAD_DIR/$DEAD_HOST
		nmap $DEAD_NMAP $DEAD_DIR/$DEAD_HOST/$DEAD_HOST $DEAD_HOST
		echo -e ""
	done < "$DEAD_HOSTS"
	echo -e "${COL1} Hosts Scanned"
	cat ${DEAD_HOSTS}
	echo -e "\n${COL1} Output Files - Located at\n${COL1} ${DEAD_DIR}"
	ls -la $DEAD_DIR
	exit
fi
rm -rf $DEAD_DIR
echo -e "${COL1} Exiting..\n"
exit
