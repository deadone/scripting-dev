#!/bin/bash
# author: dead1
# quick script to scan network machines for different SMB vulns

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

scan_vuln() {
	echo -e "${NICED} Starting Nmap Network Enumeration Scan - Please be patient."
	nmap -p${NMAP_PORT} -Pn ${NET_TO_SCAN} > enum.scan
	cat enum.scan | grep -B 4 open | grep for | cut -b 22-40 > ${NMAP_PORT}.scan
	HOST_WC=`cat ${NMAP_PORT}.scan | wc | cut -d " " -f 6`
	rm enum.scan
	echo -e "${NICED} ${DRED}${HOST_WC}${NC} Hosts Running Port ${DYEL}${NMAP_PORT}${NC} on ${DYEL}${NET_TO_SCAN}${NC}:"
	cat ${NMAP_PORT}.scan
	echo -e "\n${NICED} Starting ${DRED}${NMAP_SCRIPT}${NC} Scan Against Them - Please be patient."	

	nmap -Pn -p${NMAP_PORT} --open --max-hostgroup 3 --script ${NMAP_SCRIPT} -iL ${NMAP_PORT}.scan > vuln.out
	rm ${NMAP_PORT}.scan
	cat vuln.out | grep -i -B 8 -A 4 vulnerable >  ${FIND_VULN}-vuln.out
	rm vuln.out
	echo -e "${NICED} Vulnerable Targets:${DRED}"
	cat ${FIND_VULN}-vuln.out | grep for | cut -b 22-40
	## comment following (1) lines out to create log
	rm ${FIND_VULN}-vuln.out
}

LOG_DATE=`date +"%D - %T"`
echo -e "${DGRN}>>> Dead1's OSCP Network Vuln Scan <<<"
echo -e "${DBLU}${LOG_DATE}${NC}"
scan_vuln
## uncomment line below for log
#echo -e "${NC}Log Created: ${DGRN}${PWD}/${FIND_VULN}-vuln.out${NC}\n"
echo -e "${NC}"
exit
