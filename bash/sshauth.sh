#!/bin/bash
# Author: dead1
# Script to Log SSH Authorization Attempts
# Parses Fail2ban.log and Auth.log
# Requires Fail2ban to be installed
# Username Attempts / IP Addresses
# Writes to GODLOG everytime script is ran

# Filename Output Variables to be found in logs/
TRYNAME="tried.log"  # output filename for username attempts
BANNAME="banned.log" # output filename for banned IPs
GODLOG="godlog.log"  # updates with time script is ran

mkdir -p $PWD/logs
cat /var/log/auth.log* | grep ssh | grep invalid | cut -b 75-150 | cut -d " " -f 3 > $PWD/logs/temp1
sort $PWD/logs/temp1 | uniq > $PWD/logs/$TRYNAME
zgrep 'Ban' /var/log/fail2ban.log* | cut -b 75-150 | cut -d " " -f 6 > $PWD/logs/temp2
sort $PWD/logs/temp2 | uniq > $PWD/logs/$BANNAME
sed -i '/^$/d' $PWD/logs/$TRYNAME
rm $PWD/logs/temp*
sed -i '/^$/d' $PWD/logs/$BANNAME
LLDATE=`date`
USERT=`wc -w $PWD/logs/$TRYNAME | cut -d " " -f 1`
BANNT=`wc -w $PWD/logs/$BANNAME | cut -d " " -f 1`
echo -e "${LLDATE}\tUsernames: ${USERT}\tBanned: ${BANNT}" >> $PWD/logs/$GODLOG
echo -e "\n *SSH Server Authentication Stats*"
echo -e "  [ ${BANNT} ] Banned IPs\n  [ ${USERT} ] Attempted Usernames"
echo -e " Logs Located:"
echo -e "  $PWD/logs/$GODLOG\n  $PWD/logs/${BANNAME}\n  $PWD/logs/${TRYNAME}\n"
