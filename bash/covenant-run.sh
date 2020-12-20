#!/bin/bash
DRED='\033[1;31m' #red
NC='\033[0m' #color off
if [ "$EUID" -ne 0 ]
  then echo "${DRED}[x] Run as root.${NC}"
  exit
fi
echo -e "${DRED}[*] Starting Covenant.${NC}"
current=$PWD
cd /opt/Covenant/Covenant
echo -e "${DRED}[*] Press Ctrl+C to stop.${NC}"
dotnet run
cd $current
echo -e "\n${DRED}[*] Exiting.${NC}"
