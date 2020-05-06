#!/bin/bash
# author: dead1
# quick script to scan network machines for different SMB vulns
# run examples:
# ./deadmap-vuln.sh (to run standalone, you need to properly edit NET_TO_SCAN)
# ./deadmap-vuln.sh 10.11.1.0/24

### SMB Vuln Scripts
# smb-vuln-conficker.nse
# smb-vuln-cve2009-3103.nse
# smb-vuln-cve-2017-7494.nse
# smb-vuln-ms17-010.nse
# smb-vuln-ms06-025.nse
# smb-vuln-ms07-029.nse
# smb-vuln-ms08-067.nse
# smb-vuln-ms10-054.nse
# smb-vuln-ms10-061.nse

# input network to scan here
NET_TO_SCAN="10.11.1.0/24"		# network array to scan
FIND_VULN="ms17-010" 			# name of vuln
NMAP_SCRIPT="smb-vuln-ms17-010"		# nmap script to run
NMAP_PORT=445				# port scan runs on

# colours
DRED='\033[1;31m' #light red
DBLU='\033[0;34m' #light blue
DYEL='\033[1;33m' #yellow
DGRN='\033[0;32m' #green
NC='\033[0m' #color off
NICED="${DGRN}[*]${NC}"

if [ "$1" == "" ]
then
	:
else
	NET_TO_SCAN=${1}
fi

LOG_DATE=`date +"%D - %T"`
echo -e "${DGRN}>>> Dead1s OSCP Network Vuln Scan <<<"
echo -e "${DBLU}${LOG_DATE}${NC}"
echo -e "${NICED} Searching on:\t${DYEL}${NET_TO_SCAN}${NC}"
echo -e "${NICED} Searching for:\t${DRED}${FIND_VULN}${NC}"
echo -e "${NICED} Starting Network Enumeration Scan - Please be patient..."
nmap -p ${NMAP_PORT} -sT -Pn ${NET_TO_SCAN} > /tmp/enum.scan
cat /tmp/enum.scan | grep -B 4 open | grep -i "for" | cut -b 22-40 > /tmp/${NMAP_PORT}.scan
HOST_WC=`cat /tmp/${NMAP_PORT}.scan | wc -l` 
rm /tmp/enum.scan
if [ "$HOST_WC" == "" ]
then
	echo -e "${DRED}No Hosts Found Running Port ${NMAP_PORT}! Check the Network.${NC}"
	rm /tmp/${NMAP_PORT}.scan
	exit
fi
echo -e "${NICED} ${DYEL}${HOST_WC}${NC} Hosts Running Port ${DYEL}${NMAP_PORT}${NC}"
# cat /tmp/${NMAP_PORT}.scan # uncomment to view hosts with open ports
echo -e "${NICED} Starting ${DRED}${NMAP_SCRIPT}${NC} Scan Against ${DYEL}${HOST_WC}${NC} Hosts - Please be patient..."	
nmap -p ${NMAP_PORT} -sT -Pn --open --max-hostgroup 3 --script ${NMAP_SCRIPT} -iL /tmp/${NMAP_PORT}.scan > /tmp/vuln.out
rm /tmp/${NMAP_PORT}.scan
cat /tmp/vuln.out | grep -i -B 8 -A 4 vulnerable > /tmp/${FIND_VULN}-vuln.out
rm /tmp/vuln.out
echo -e "${NICED} Vulnerable Targets:${DRED}"
cat /tmp/${FIND_VULN}-vuln.out | grep -i "for" | cut -b 22-40
VULN_TART=`cat /tmp/${FIND_VULN}-vuln.out | grep -i "for" | cut -b 22-40`
if [ "$VULN_TART" == "" ] 
then
	echo -e "${DRED}None Vulnerable.${NC}"
fi
rm /tmp/${FIND_VULN}-vuln.out
echo -e "${NC}"
exit
