#!/bin/bash
# Author: dead1
# Script to Log SSH Authorization Attempts
# Parses Fail2ban.log and Auth.log
# Requires Fail2ban to be installed
# Username Attempts / IP Addresses
# Writes to GODLOG everytime script is ran

# Variables
DIRNAME="sshlogs"    # directory used/created for output
TRYNAME="tried.log"  # output filename for username attempts
BANNAME="banned.log" # output filename for banned IPs
GODLOG="godlog.log"  # chronological output file
DISLOG=5             # number of logs to display

clear
mkdir -p $PWD/$DIRNAME
zgrep 'Invalid' /var/log/auth.log* | cut -b 75-150 | cut -d " " -f 2 > $PWD/$DIRNAME/temp1
zgrep 'Ban' /var/log/fail2ban.log* | cut -b 75-150 | cut -d " " -f 6 > $PWD/$DIRNAME/temp2
sort $PWD/$DIRNAME/temp1 | uniq > $PWD/$DIRNAME/$TRYNAME
sort $PWD/$DIRNAME/temp2 | uniq > $PWD/$DIRNAME/$BANNAME
sed -i '/^$/d' $PWD/$DIRNAME/$TRYNAME
sed -i '/^$/d' $PWD/$DIRNAME/$BANNAME
rm $PWD/$DIRNAME/temp*
LLDATE=`date`
USERT=`wc -w $PWD/$DIRNAME/$TRYNAME | cut -d " " -f 1`
BANNT=`wc -w $PWD/$DIRNAME/$BANNAME | cut -d " " -f 1`
LUSRS=0
LBANS=0
echo -e "\n *SSH Server Authentication Stats*"
echo -e "  [ ${BANNT} ] Banned IPs\n  [ ${USERT} ] Attempted Usernames"
GODFILE="${PWD}/${DIRNAME}/${GODLOG}"
if [ -f "$GODFILE" ]; then
	LUSRS=`tail -n 1 $GODFILE | cut -d " " -f 9`
	LBANS=`tail -n 1 $GODFILE | cut -d " " -f 15`
	echo -e "  [ $(($USERT-$LUSRS)) ] New Usernames\n  [ $(($BANNT-$LBANS)) ] New IPs"
fi
echo -e " Logs Located:"
echo -e "  ${PWD}/${DIRNAME}/${GODLOG}\n  ${PWD}/${DIRNAME}/${BANNAME}\n  ${PWD}/${DIRNAME}/${TRYNAME}\n"
echo -e " Last [ ${DISLOG} ] Logs"
echo -e "${LLDATE} [Total Usernames: ${USERT} / New: $(($USERT-$LUSRS))] [Total Banned: ${BANNT} / New: $(($BANNT-$LBANS))]" >> $PWD/$DIRNAME/$GODLOG
cat $PWD/$DIRNAME/$GODLOG | tail -n $DISLOG
echo -e ""
