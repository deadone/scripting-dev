#!/usr/bin/python3
# Filename: deadlib.py
# Author: dead1
# Details: class library
import os

class color:
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    magenta = "\x1b[35m"
    cyan = "\x1b[36m"
    lightgray = "\x1b[37m"
    darkgray = "\x1b[90m"
    lightred = "\x1b[91m"
    lightgreen = "\x1b[92m"
    lightyellow = "\x1b[93m"
    lightblue = "\x1b[94m"
    pink = "\x1b[95m"
    lightcyan = "\x1b[96m"
    white = "\x1b[97m"
    bold = '\033[1m' # bold
    nc ='\x1b[0m' # No Color

def colrep(repeat):
    if repeat == 0: return color.red
    if repeat == 1: return color.blue
    if repeat == 2: return color.lightblue
    if repeat == 3: return color.yellow
    if repeat == 4: return color.green
    if repeat == 5: return color.cyan
    if repeat == 6: return color.lightcyan
    if repeat == 7: return color.pink
    if repeat > 7: return color.nc


class LinuxProcList:
    def linuxGetProc():
        proc = os.popen('ls /proc/').read()
        procList = proc.split("\n")
        newProc = []
        for x in range(len(procList)):
            if procList[x].isdigit():
                newProc.append(int(procList[x]))
        newProc.sort()
        return newProc

    def verifyPid(pid):
        pid = str(pid)
        processes = LinuxProcList.linuxGetProc()
        for x in range(len(processes)):
            if pid in str(processes[x]):
                return True

    def getName(pid):
        pid = str(pid)
        name = "No Name"
        if LinuxProcList.verifyPid(pid):
            statusStr = "/proc/" + pid + "/status"
            status = open(statusStr, "r")
            status = status.read()
            status = status.split("\n")
            for x in range(len(status) - 1):
                status[x] = status[x].split("\t")
                status[x][1] = status[x][1].replace(" ", "")
            for x in range(len(status)):
                if 'Name:' in status[x]:
                    name = status[x][1]
                    break
            return name
        else:
            return name

    def proclist():
        return LinuxProcList.linuxGetProc()

    def proclistPlus():
        processes = LinuxProcList.linuxGetProc()
        counter = 0
        print(color.bold + color.red + str(len(processes)), "Current Running Proccesses:" + color.nc)
        for x in range(len(processes)):
            if counter == 4:
                print()
                counter = 1
            else:
                counter += 1
            print((color.blue + str(processes[x]) + color.nc + " ").ljust(16, "-") + ">>", color.bold + LinuxProcList.getName(processes[x])[0:15].ljust(15, " "),color.nc, end="  ")
        print()

    def cmdline(pid):
        pid = str(pid)
        if LinuxProcList.verifyPid(pid):
            procString = "cat /proc/" + pid + "/cmdline"
            if len(os.popen(procString).read()) != 0:
                cmd = os.popen(procString).read()
                cmd = cmd.replace("\0", " ")
                return cmd
            else:
                return None
        else:
            return None

    def children(pid):
        pid = str(pid)
        if LinuxProcList.verifyPid(pid):
            procString = "cat /proc/" + pid + "/task/" + pid + "/children"
            if os.popen(procString).read() != "":
                children = os.popen(procString).read()
                children = children.split(" ")
                children.pop()
                return children
            else:
                return None
        else:
            return None


class LinuxProcess:
    def __init__(self, pidStr):
        statStr = "/proc/" + pidStr + "/stat"
        statusStr = "/proc/" + pidStr + "/status"
        self.stat = open(statStr, "r")
        self.stat = self.stat.read()
        self.status = open(statusStr, "r")
        self.status = self.status.read()
        self.statList = self.stat.split(" ")
        self.statusList = self.status.split("\n")
        for x in range(len(self.statusList) - 1):
            self.statusList[x] = self.statusList[x].split("\t")
            self.statusList[x][1] = self.statusList[x][1].replace(" ", "")

    def name(self):
        name = "error."
        for x in range(len(self.statusList)):
            if 'Name:' in self.statusList[x]:
                name = self.statusList[x][1]
                break
        return name

    def pid(self):
        pid = "error."
        for x in range(len(self.statusList)):
            if 'Pid:' in self.statusList[x]:
                pid = self.statusList[x][1]
                break
        return pid

    def state(self):
        state = "error."
        for x in range(len(self.statusList)):
            if 'State:' in self.statusList[x]:
                state = self.statusList[x][1]
                break
        return state

    def ppid(self):
        ppid = "error."
        for x in range(len(self.statusList)):
            if 'PPid:' in self.statusList[x]:
                ppid = self.statusList[x][1]
                break
        return ppid

    def rss(self):
        rss = self.statList[23]
        return hex(int(rss))

    def rssLimit(self):
        rssLimit = self.statList[24]
        return hex(int(rssLimit))

    def startCode(self):
        startCode = self.statList[25]
        return hex(int(startCode))

    def endCode(self):
        endCode = self.statList[26]
        return hex(int(endCode))

    def stackStart(self):
        stackStart = self.statList[27]
        return hex(int(stackStart))

    def startData(self):
        startData = self.statList[44]
        return hex(int(startData))

    def endData(self):
        endData = self.statList[45]
        return hex(int(endData))

    def startBrk(self):
        startBrk = self.statList[46]
        return hex(int(startBrk))

    def argStart(self):
        argStart = self.statList[47]
        return hex(int(argStart))

    def argEnd(self):
        argEnd = self.statList[48]
        return hex(int(argEnd))

    def envStart(self):
        envStart = self.statList[49]
        return hex(int(envStart))

    def envEnd(self):
        envEnd = self.statList[50]
        return hex(int(envEnd))
