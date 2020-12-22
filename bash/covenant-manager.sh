#!/bin/bash
# author: dead1
# 2020-12-21
# manage covenant installs
# install / backup / run / uninstall
# to add: uninstall

# colour codes
DRED='\033[1;31m' #red
LGRN='\033[0;32m' #green
NC='\033[0m' #color off

func_run() {
    echo -e "[*] Starting Covenant."
    cd /opt/Covenant/Covenant
    echo -e "${DRED}[!] Press Ctrl+C to stop.${NC}"
    dotnet run
    echo -e ""
}

func_install() {
    echo -e "[*] Installing Covenant."
    cd /opt/
    wget -q https://packages.microsoft.com/config/ubuntu/19.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    sudo dpkg -i packages-microsoft-prod.deb &>/dev/null
    sudo apt -y update &>/dev/null
    echo -e "[*] Downloading apt-transport-https"
    sudo apt -y install apt-transport-https &>/dev/null
    sudo apt -y update &>/dev/null
    echo -e "[*] Downloading dotnet-sdk-3.1"
    sudo apt -y install dotnet-sdk-3.1 &>/dev/null
    echo -e "[*] Downloading Covenant."
    sudo git clone --recurse-submodules https://github.com/cobbr/Covenant.git /opt/Covenant &>/dev/null
    mv /opt/packages-microsoft-prod.deb /opt/Covenant/
    cd /opt/Covenant/Covenant
    dotnet build | grep -i "Build succeeded"
    echo -e "${LGRN}[*] Installation complete!${NC}"
    echo -ne "${DRED}[!] Do you want to start Covenant? (y/n):${NC} "
    read autostart
    if [ $autostart = "y" ]
    then
            dotnet run
    fi
}

func_refresh() {
    echo -ne "${DRED}[!] Do you want to backup existing installation? (y/n):${NC} "
    read backup_q
    if [ $backup_q = 'y' ]
    then
        func_createbackup
    fi
    rm -rf /opt/Covenant
    echo -e "[*] Downloading fresh installation."
    sudo git clone --recurse-submodules https://github.com/cobbr/Covenant.git /opt/Covenant &>/dev/null
    cd /opt/Covenant/Covenant/
    echo -e "[*] Building .NET framework.${LGRN}"
    dotnet build | grep -i "Build succeeded"
    echo -e "${LGRN}[*] Fresh installation complete!${NC}"
    echo -ne "${DRED}[!] Do you want to start Covenant? (y/n):${NC} "
    read autostart
    if [ $autostart = "y" ]
    then
            dotnet run
    fi
}

func_createbackup() {
    echo -ne "${DRED}[!] Job name:${NC} "
    read the_job
    the_date=`date +"%d-%m-%y"`
    echo -e "[*] Compressing existing installation of Covenant."
    tar -czvf  /tmp/Covenant-${the_job}-${the_date}.tar.gz /opt/Covenant &>/dev/null
    echo -e "[*] Backup of installation located @${LGRN} /tmp/Covenant-${the_job}-${the_date}${NC}"
}

func_delbackup() {
    echo -e "[*] Deleting Backups."
    rm -rf /tmp/Covenant-*
}

if [ "$EUID" -ne 0 ]
  then echo "${DRED}[x] Run as root.${NC}"
  exit
fi

current=$PWD
num_backups=`ls /tmp/ | grep "Covenant" | wc | cut -d " " -f 7`
installed="${DRED}False${NC}"
if [ -d "/opt/Covenant" ]
then
    installed="${LGRN}True${NC}"
fi

echo -e "${DRED}-= Covenant Manager =-${NC}"
echo -e " Installed: \t${installed}"
echo -e " # Backups: \t${num_backups}"
echo -e "\n [${LGRN}1${NC}] Run\n [${LGRN}2${NC}] Install\n [${LGRN}3${NC}] Fresh Install${NC}\n [${LGRN}4${NC}] Create Backup\n [${LGRN}5${NC}] Delete Backups\n [${LGRN}6${NC}] Exit"
echo -ne "${DRED}\nSelection:${NC} "
read the_choice
echo -e ""

case $the_choice in
    1)
        func_run
        ;;

    2)
        func_install
        ;;

    3)
        func_refresh
        ;;

    4)
        func_createbackup
        ;;

    5)
        func_delbackup
        ;;

    6)
        echo -e "${DRED}\n[!] Exiting.${NC}"
        exit
        ;;

    *)
        echo -e "${DRED}[X] Invalid Selection.${NC}"
        exit
        ;;
esac 

cd $current
echo -e "${LGRN}[!] Done.${NC}"
