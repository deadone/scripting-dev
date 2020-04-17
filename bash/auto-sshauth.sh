#!/bin/bash
# Author: dead1
# Script to Log SSH Authorization Attempts
# Parses Fail2ban.log and Auth.log
# Requires Fail2ban to be installed
# Username Attempts / IP Addresses
# Writes to GODLOG everytime script is ran

# Script Variables
DIRNAME="sshlogs"    # directory used/created for output
TRYNAME="tried.log"  # output filename for username attempts
BANNAME="banned.log" # output filename for banned IPs
GODLOG="godlog.log"  # chronological output file
SLPTME=1800          # seconds (3600 = 1h)
DISLOG=10            # number of logs to display

# Time Sync
# Generates Cleaner Logging:
# Finds the next half-hour or hour to sync the start of the script
# change value to false to remove
DO_SYNC=true

function time_sync {
        clear
        local TS_START=$(date +%s)
        local TS_INI=$(($TS_START/1800))
        local TS_MOD=$(($TS_INI+1))
        local TS_FIN=$(($TS_MOD*1800))
        local TS_SLP=$(($TS_FIN-$TS_START))
        local RIGHT_NOW=`date`
        local NEXT_TIME=`date -d @${TS_FIN}`
        echo -e "\n >> Time Sync <<"
	echo -e " Managing Script Start Times"
        echo -e " Current Time:\t${RIGHT_NOW}"
        echo -e " Start Time:\t${NEXT_TIME}"
        echo -e " Countdown:\t${TS_SLP} Seconds"
        echo -e "\n Press Ctrl+C to Cancel"
        sleep $TS_SLP
}

if [ "$DO_SYNC" = "true" ]; then
        time_sync
fi

while [ 1 ]
do
	LLDATE=`date`
	clear
	mkdir -p $PWD/$DIRNAME
	zgrep 'Invalid' /var/log/auth.log* | cut -b 75-150 | cut -d " " -f 2 > $PWD/$DIRNAME/temp1
	zgrep 'Ban' /var/log/fail2ban.log* | cut -b 75-150 | cut -d " " -f 6 > $PWD/$DIRNAME/temp2
	sort $PWD/$DIRNAME/temp1 | uniq > $PWD/$DIRNAME/$TRYNAME
	sort $PWD/$DIRNAME/temp2 | uniq > $PWD/$DIRNAME/$BANNAME
	sed -i '/^$/d' $PWD/$DIRNAME/$TRYNAME
	sed -i '/^$/d' $PWD/$DIRNAME/$BANNAME
	rm $PWD/$DIRNAME/temp*
	USERT=`wc -w $PWD/$DIRNAME/$TRYNAME | cut -d " " -f 1`
	BANNT=`wc -w $PWD/$DIRNAME/$BANNAME | cut -d " " -f 1`
	LUSRS=0
	LBANS=0
	echo -e "\n >> SSH Server Authentication Stats <<"
	echo -e " Setup to Log Every: [ $((${SLPTME}/60)) Minutes ]"
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
	echo -e "\n Press Ctrl+C to Exit"
	sleep $SLPTME
done
