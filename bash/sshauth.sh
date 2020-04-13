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

mkdir -p $PWD/$DIRNAME
cat /var/log/auth.log* | grep ssh | grep invalid | cut -b 75-150 | cut -d " " -f 3 > $PWD/$DIRNAME/temp1
sort $PWD/$DIRNAME/temp1 | uniq > $PWD/$DIRNAME/$TRYNAME
zgrep 'Ban' /var/log/fail2ban.log* | cut -b 75-150 | cut -d " " -f 6 > $PWD/$DIRNAME/temp2
sort $PWD/$DIRNAME/temp2 | uniq > $PWD/$DIRNAME/$BANNAME
rm $PWD/$DIRNAME/temp*
sed -i '/^$/d' $PWD/$DIRNAME/$TRYNAME
sed -i '/^$/d' $PWD/$DIRNAME/$BANNAME
LLDATE=`date`
USERT=`wc -w $PWD/$DIRNAME/$TRYNAME | cut -d " " -f 1`
BANNT=`wc -w $PWD/$DIRNAME/$BANNAME | cut -d " " -f 1`
echo -e "${LLDATE}\tUsernames: ${USERT}\tBanned: ${BANNT}" >> $PWD/$DIRNAME/$GODLOG
echo -e "\n *SSH Server Authentication Stats*"
echo -e "  [ ${BANNT} ] Banned IPs\n  [ ${USERT} ] Attempted Usernames"
echo -e " Logs Located:"
echo -e "  ${PWD}/$DIRNAME/${GODLOG}\n  ${PWD}/$DIRNAME/${BANNAME}\n  ${PWD}/$DIRNAME/${TRYNAME}\n"
echo -e " Godlog:"
cat $PWD/$DIRNAME/$GODLOG
echo -e ""
