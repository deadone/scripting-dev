#!/bin/bash
DRED='\033[1;31m' #red
NC='\033[0m' #color off
if [ "$EUID" -ne 0 ]
  then echo "${DRED}[x] Run as root.${NC}"
  exit
fi
echo -e "${DRED}[*] Installing Covenant.${NC}"
read autostart
current=$PWD
cd /opt/
wget -q https://packages.microsoft.com/config/ubuntu/19.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt -y update
sudo apt -y install apt-transport-https
sudo apt -y update
sudo apt -y install dotnet-sdk-3.1
rm packages-microsoft-prod.deb
sudo git clone --recurse-submodules https://github.com/cobbr/Covenant.git /opt/Covenant
cd /opt/Covenant/Covenant
dotnet build
echo -n "${DRED}[*] Do you want to start Covenant? [y/n] : ${NC}"
if [ $autostart = "y" ]
        dotnet run
fi
cd $current
echo -e "${DRED}[*] Done.${NC}"
