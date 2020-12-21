#!/bin/bash
DRED='\033[1;31m' #red
NC='\033[0m' #color off
current=$PWD
date=`date`
if [ "$EUID" -ne 0 ]
  then echo "${DRED} [x] Run as root.${NC}"
  exit
fi
echo -e "${DRED} [*] Backing up and compressing existing installation of Covenant.${NC}"
echo -e "${DRED} [*] This will take a moment.${NC}"
tar -czvf  /tmp/Covenant-backup-${DATE}.tar.gz /opt/Covenant &>/dev/null
rm -rf /opt/Covenant
echo -e "${DRED} [*] Downloading fresh installation.${NC}"
sudo git clone --recurse-submodules https://github.com/cobbr/Covenant.git /opt/Covenant
cd /opt/Covenant/Covenant/
dotnet build
cd $current
echo -e "\n${DRED} [*] Installation complete. Backup of old installation located @${NC} /tmp/Covenant-backup-${DATE}"
