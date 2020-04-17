#!/bin/bash
# Time Sync
# Author: dead1
# Program to execute command/script/program at proper intervals
# On the day, hour, half-hour or minute.

TZ=6 # hours behind UTC
DELTA_REP=$1
TZ_OFFSET=0
case $2 in
day)
	DELTA_TIME=86400
	TZ_OFFSET=$(($TZ*3600))
	;;
hour)
	DELTA_TIME=3600
	;;
half)
	DELTA_TIME=1800
	;;
min)
	DELTA_TIME=60
	;;
*)
	echo -e "Correct Usage:\n ./timesync 1 day \"./script-to-execute.sh arg1 arg2\"\tStart scrpt on 'n'th day (1 = next day)"
	echo -e " ./timesync 1 hour \"./script-to-execute.sh arg1 arg2\"\tStart script on 'n' hour (1 = next hour)"
	echo -e " ./timesync 1 half \"./script-to-execute.sh arg1 arg2\"\tStart script on 'n'th half-hour (1 = next half-hour)"
	echo -e " ./timesync 1 min \"./script-to-execute.sh arg1 arg2\"\tStart script on next 'n'th minute (1 = next minute)"
	echo -e " ./timesync 1 min \"ls -la\"\n"
	exit
	;;
esac

clear
TS_START=$(date +%s)
TS_INI=$(($TS_START/$DELTA_TIME))
TS_MOD=$(($TS_INI+$DELTA_REP))
TS_FIN=$((($TS_MOD*$DELTA_TIME) + TZ_OFFSET))
TS_SLP=$(($TS_FIN-$TS_START))
RIGHT_NOW=`date`
NEXT_TIME=`date -d @${TS_FIN}`
echo -e "\n >> Time Sync <<"
echo -e " Managing Execution Start Times"
echo -e " Current Time:\t${RIGHT_NOW}"
echo -e " Start Time:\t${NEXT_TIME}"
echo -e " Countdown:\t${TS_SLP} Seconds"
echo -e "\n Command to Execute:\n ${3}"
echo -e "\n Press Ctrl+C to Cancel\n"
sleep $TS_SLP
$3
