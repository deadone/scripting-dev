#!/bin/bash
# Time Sync
# Author: dead1
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
        echo -e " Current Time:\t${RIGHT_NOW}"
        echo -e " Start Time:\t${NEXT_TIME}"
        echo -e " Countdown:\t${TS_SLP} Seconds"
        echo -e "\n Press Ctrl+C to Cancel"
        sleep $TS_SLP
}

if [ "$DO_SYNC" = "true" ]; then
        time_sync
fi
