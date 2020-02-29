#!/usr/bin/python3
# Filename: deadlib.py
# Author: dead1
# Details: class library
import os


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
        name = "NoName"
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
        print(len(processes),"Current Running Proccesses:")
        for x in range(len(processes)):
            if counter == 6:
                print()
                counter = 1
            else:
                counter += 1
            print(str(processes[x]).rjust(7, " "),LinuxProcList.getName(processes[x])[0:12].rjust(14, " "), end=" ")
        print()

    def cmdline(pid):
        pid = str(pid)
        if LinuxProcList.verifyPid(pid):
            procString = "cat /proc/" + pid + "/cmdline"
            if len(os.popen(procString).read()) != 0:
                return os.popen(procString).read()
            else:
                return None
        else:
            return None

    def children(pid):
        pid = str(pid)
        if LinuxProcList.verifyPid(pid):
            procString = "ps --ppid " + pid
            if os.popen(procString).read() != 0:
                children = os.popen(procString).read()
                if len(children) <= 30:
                    return None
                else:
                    children = children.split("\n")
                    newchildren = []
                    for x in range(1, len(children)):
                        children[x] = children[x][0:8]
                        children[x] = children[x].replace(" ", "")
                        newchildren.append(children[x].replace("  ", ""))
                    newchildren.pop()
                    return newchildren
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
