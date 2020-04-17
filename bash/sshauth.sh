#!/bin/bash
# Author: dead1
# SSH Authorization Attempts
# Parses Fail2ban.log and Auth.log
# Requires Fail2ban to be installed
# Username Attempts / IP Addresses

# Variables
DIRNAME="auth-ssh"  # directory used/created for output
TRYNAME="user.log"  # output filename for username attempts
BANNAME="ip.log"    # output filename for banned IPs

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
echo -e "\n >> SSH Server Authentication Stats <<"
echo -e "  [ ${BANNT} ] Banned IPs\n  [ ${USERT} ] Attempted Usernames"
echo -e " Logs Created:"
echo -e "  ${PWD}/${DIRNAME}/${BANNAME}\n  ${PWD}/${DIRNAME}/${TRYNAME}\n"
