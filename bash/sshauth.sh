#!/bin/bash
# Author: dead1
# SSH Authorization Attempts
# Parses Fail2ban.log (if enabled) and Auth.log
# Username Attempts / IP Addresses

# Variables
TRYNAME="user.log"  # output filename for username attempts
BANNAME="ip.log"    # output filename for banned IPs (if fail2ban is enabled)

echo -e " >> SSH Server Authentication Stats <<"
if [ -f "/var/log/auth.log" ]; then
    zgrep 'Invalid' /var/log/auth.log* | cut -b 75-150 | cut -d " " -f 2 > $PWD/temp1
	sort $PWD/temp1 | uniq > $PWD/$TRYNAME
	sed -i '/^$/d' $PWD/$TRYNAME
	rm $PWD/temp1
	USERT=`wc -w $PWD/$TRYNAME | cut -d " " -f 1`
	echo -e "  [ ${USERT} ] Attempted Usernames"
	echo -e " \tLog Created: ${PWD}/${TRYNAME}"
fi

if [ -f "/var/log/fail2ban.log" ]; then
    zgrep 'Ban' /var/log/fail2ban.log* | cut -b 75-150 | cut -d " " -f 6 > $PWD/temp2
	sort $PWD/temp2 | uniq > $PWD/$BANNAME
	sed -i '/^$/d' $PWD/$BANNAME
	rm $PWD/temp2
	BANNT=`wc -w $PWD/$BANNAME | cut -d " " -f 1`
	echo -e "  [ ${BANNT} ] Banned IPs"
	echo -e "\tLog Created: ${PWD}/${BANNAME}"
fi
echo -e ""
