#!/bin/bash
# author: dead1
# quick script to scan network machines for certain port
# run examples:
# ./deadmap-quikport.sh (to run standalone, you need to properly edit NET_TO_SCAN)
# ./deadmap-quikport.sh 10.11.1.0/24

# input network to scan here
NET_TO_SCAN="10.11.1.0/24"		# network array to scan
NMAP_PORT=22				# port scan runs on

# colours
DRED='\033[1;31m' #light red
DBLU='\033[0;34m' #light blue
DYEL='\033[1;33m' #yellow
DGRN='\033[0;32m' #green
NC='\033[0m' #color off
NICED="${DGRN}[*]${NC}"
LOG_DATE=`date +"%D - %T"`

if [ "$1" == "" ]
then
	:
else
	NET_TO_SCAN=${1}
fi
if [ "$2" == "" ]
then
	:
else
	NMAP_PORT=${2}
fi
echo -e "${DGRN}>>> Dead1s OSCP Quick Port Scan <<<"
echo -e "${DBLU}${LOG_DATE}${NC}"
echo -e "${NICED} Searching on:\t${DYEL}${NET_TO_SCAN}${NC}"
echo -e "${NICED} Searching for:\t${DYEL}${NMAP_PORT}${NC}"
echo -e "${NICED} Starting Enumeration Scan - Please be patient..."
nmap -p ${NMAP_PORT} -sT -Pn ${NET_TO_SCAN} > /tmp/enum.scan
cat /tmp/enum.scan | grep -B 4 open | grep -i "for" | cut -b 22-40 > /tmp/${NMAP_PORT}.scan
HOST_WC=`cat /tmp/${NMAP_PORT}.scan | wc -l`
if [ "$HOST_WC" == "" ]
then
	echo -e "${DRED}No Hosts Found Running Port ${NMAP_PORT}! Check the Network.${NC}"
	rm /tmp/${NMAP_PORT}.scan
	exit
fi
rm /tmp/enum.scan
echo -e "${NICED} ${DYEL}${HOST_WC}${NC} Hosts Running Port ${DYEL}${NMAP_PORT}${DRED}"
cat /tmp/${NMAP_PORT}.scan
echo -e "${NC}"
rm /tmp/${NMAP_PORT}.scan
exit
