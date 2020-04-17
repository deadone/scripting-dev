#!/bin/bash
# Function Time Sync
# Author: dead1
# Bash function to help manage time sync with execution
# Generates proper sleep parameter for next exectuion
# Used to generate cleaner logs and program syncing

# change value to false to remove
DO_SYNC=true	
SLPTIME=1800	# in seconds, used for frequency of execution

function time_sync {
        local TS_START=$(date +%s)
        local TS_INI=$(($TS_START/$SLPTME))
        local TS_MOD=$(($TS_INI+1))
        local TS_FIN=$(($TS_MOD*$SLPTME))
        local TS_SLP=$(($TS_FIN-$TS_START))
        sleep $TS_SLP
}

if [ "$DO_SYNC" = "true" ]; then
        time_sync
fi
