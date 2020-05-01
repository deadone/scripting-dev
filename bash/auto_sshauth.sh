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
SLPTME=3600          # seconds (3600 = 1h)
DISLOG=13            # number of logs to display

function time_sync {
        local TS_START=$(date +%s)
        local TS_INI=$(($TS_START/$SLPTME))
        local TS_MOD=$(($TS_INI+1))
        local TS_FIN=$(($TS_MOD*$SLPTME))
        local TS_SLP=$(($TS_FIN-$TS_START))
        sleep $TS_SLP
}

# colours
DRED='\033[1;31m' #light red
DBLU='\033[0;34m' #light blue
DYEL='\033[1;33m' #yellow
DGRN='\033[0;32m' #green
NC='\033[0m' #color off

while [ 1 ]
do
        LLDATE=`date +"%m-%d-%y %r"`
        LLTIME=`date +"%r"`
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
        echo -e "\n  ${DRED}>> Dead1's SSH Server Authentication Stats <<${NC}"
        echo -e "  Current Server Time:\t\t[ ${DBLU}$LLTIME${NC} ]"
        echo -e "  Setup to Log Every:\t\t[ ${DBLU}$((${SLPTME}/60)) Minutes${NC} ]"
        echo -e "  # of Banned IPs\t\t[ ${DGRN}${BANNT}${NC} ]\n  # of Attempted Usernames\t[ ${DGRN}${USERT}${NC} ]"
        GODFILE="${PWD}/${DIRNAME}/${GODLOG}"
        if [ -f "$GODFILE" ]; then
                LUSRS=`tail -n 1 $GODFILE | cut -d " " -f 5`
                LBANS=`tail -n 1 $GODFILE | cut -d " " -f 10`
                echo -e "  # of New Usernames\t\t[ ${DRED}$(($USERT-$LUSRS))${NC} ]\n  # of New IPs\t\t\t[ ${DRED}$(($BANNT-$LBANS))${NC} ]"
        else
                echo -e " >> Dead'1 SSH Auth Logger v1.2 - TimeSync RealTime Logging <<" > $GODFILE
        fi
        echo -e " ${DRED}Logs Located:${NC}"
        echo -e "  ${PWD}/${DIRNAME}/${GODLOG}\n  ${PWD}/${DIRNAME}/${BANNAME}\n  ${PWD}/${DIRNAME}/${TRYNAME}\n"
        echo -e " ${DRED}Last [ ${DBLU}${DISLOG}${DRED} ] Logs${NC}"
        echo -e "[${LLDATE}] [Usernames: ${USERT} // New: $(($USERT-$LUSRS))] [Banned: ${BANNT} // New: $(($BANNT-$LBANS))]" >> $PWD/$DIRNAME/$GODLOG
        cat $PWD/$DIRNAME/$GODLOG | tail -n $DISLOG
        echo -e "\n ${DRED}Press Ctrl+C to Exit..${NC}"
        time_sync
done
