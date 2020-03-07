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

def color_repeat(repeat):
    if repeat == 0: return color.red
    if repeat == 1: return color.blue
    if repeat == 2: return color.lightblue
    if repeat == 3: return color.yellow
    if repeat == 4: return color.green
    if repeat == 5: return color.cyan
    if repeat == 6: return color.lightcyan
    if repeat == 7: return color.pink
    if repeat > 7: return color.nc


# class for processes
class linux_proc_list:
    def linux_get_proc():
        proc_read = os.popen('ls /proc/').read()
        proc_list = proc_read.split("\n")
        new_proc_list = []
        for x in range(len(proc_list)):
            if proc_list[x].isdigit():
                new_proc_list.append(int(proc_list[x]))
        new_proc_list.sort()
        return new_proc_list

    def verify_pid(pid):
        pid = str(pid)
        processes = linux_proc_list.linux_get_proc()
        for x in range(len(processes)):
            if pid in str(processes[x]):
                return True

    def get_name(pid):
        pid = str(pid)
        name = "No Name"
        if linux_proc_list.verify_pid(pid):
            status_string = "/proc/" + pid + "/status"
            status = open(status_string, "r")
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

    def proc_list():
        return linux_proc_list.linux_get_proc()

    def proc_list_plus():
        processes = linux_proc_list.linux_get_proc()
        counter = 0
        print(color.bold + color.red + str(len(processes)), "Current Running Proccesses:" + color.nc)
        for x in range(len(processes)):
            if counter == 4:
                print()
                counter = 1
            else:
                counter += 1
            print((color.blue + str(processes[x]) + color.nc + " ").ljust(16, "-") + ">>",
                  color.bold + linux_proc_list.get_name(processes[x])[0:15].ljust(15, " "), color.nc, end="  ")
        print()

    def cmd_line(pid):
        pid = str(pid)
        if linux_proc_list.verify_pid(pid):
            proc_string = "cat /proc/" + pid + "/cmdline"
            if len(os.popen(proc_string).read()) != 0:
                cmd = os.popen(proc_string).read()
                cmd = cmd.replace("\0", " ")
                return cmd
            else:
                return None
        else:
            return None

    def children(pid):
        pid = str(pid)
        if linux_proc_list.verify_pid(pid):
            proc_string = "cat /proc/" + pid + "/task/" + pid + "/children"
            if os.popen(proc_string).read() != "":
                children = os.popen(proc_string).read()
                children = children.split(" ")
                children.pop()
                return children
            else:
                return None
        else:
            return None

    def process_viewer(pid):
        if linux_proc_list.verify_pid(pid):
            process = linux_process(pid)
            print()
            print("name:".rjust(12, " "), process.name().rjust(18, " "))
            print("state:".rjust(12, " "), process.state().rjust(18, " "))
            print("pid:".rjust(12, " "), process.pid().rjust(18, " "))
            print("ppid:".rjust(12, " "), process.ppid().rjust(18, " "))
            print("rss:".rjust(12, " "), hex(int(process.rss())).rjust(18, " "))
            print("rss_limit:".rjust(12, " "), hex(int(process.rss_limit())).rjust(18, " "))
            print("start_code:".rjust(12, " "), hex(int(process.start_code())).rjust(18, " "))
            print("end_code:".rjust(12, " "), hex(int(process.end_code())).rjust(18, " "))
            print("start_stack:".rjust(12, " "), hex(int(process.stack_start())).rjust(18, " "))
            print("start_data:".rjust(12, " "), hex(int(process.start_data())).rjust(18, " "))
            print("end_data:".rjust(12, " "), hex(int(process.end_data())).rjust(18, " "))
            print("start_brk:".rjust(12, " "), hex(int(process.start_brk())).rjust(18, " "))
            print("arg_start:".rjust(12, " "), hex(int(process.arg_start())).rjust(18, " "))
            print("arg_end:".rjust(12, " "), hex(int(process.arg_end())).rjust(18, " "))
            print("env_start:".rjust(12, " "), hex(int(process.env_start())).rjust(18, " "))
            print("env_end:".rjust(12, " "), hex(int(process.env_end())).rjust(18, " "))
        else:
            print("Process is not running.")


# object class for processes and stat file
class linux_process:
    def __init__(self, process_pid):
        if linux_proc_list.verify_pid(process_pid):
            stat_str = "/proc/" + str(process_pid) + "/stat"
            self.stat = open(stat_str, "r")
            self.stat = self.stat.read()
            self.stat_list = self.stat.split(" ")
            if len(self.stat_list) == 53:
                self.stat_list[1] += " " + self.stat_list[2]
                self.stat_list.pop(2)
        else:
            print("ERROR. Invalid PID.")
            exit(-1)

    def pid(self):
        return self.stat_list[0]

    def name(self):
        return self.stat_list[1][1:-1]

    def state(self):
        return self.stat_list[2]

    def ppid(self):
        return self.stat_list[3]

    def process_gid(self):
        return self.stat_list[4]

    def session(self):
        return self.stat_list[5]

    def tty_control(self):
        return self.stat_list[6]

    def control_gid(self):
        return self.stat_list[7]

    def flags(self):
        return self.stat_list[8]

    def minor_faults(self):
        return self.stat_list[9]

    def child_minor_faults(self):
        return self.stat_list[10]

    def maj_faults(self):
        return self.stat_list[11]

    def child_maj_faults(self):
        return self.stat_list[12]

    def user_time(self):
        return self.stat_list[13]

    def kernel_time(self):
        return self.stat_list[14]

    def child_wait_time(self):
        return self.stat_list[15]

    def child_kernel_time(self):
        return self.stat_list[16]

    def priority(self):
        return self.stat_list[17]

    def nice(self):
        return self.stat_list[18]

    def num_threads(self):
        return self.stat_list[19]

    def real_value(self):
        return self.stat_list[20]

    def start_time(self):
        return self.stat_list[21]

    def virtual_size(self):
        return self.stat_list[22]

    def rss(self):
        return self.stat_list[23]

    def rss_limit(self):
        return self.stat_list[24]

    def start_code(self):
        return self.stat_list[25]

    def end_code(self):
        return self.stat_list[26]

    def stack_start(self):
        return self.stat_list[27]

    def stack_pointer(self):
        return self.stat_list[28]

    def instruction_pointer(self):
        return self.stat_list[29]

    def pending_signal(self):
        return self.stat_list[30]

    def blocked_signals(self):
        return self.stat_list[31]

    def sig_ignore(self):
        return self.stat_list[32]

    def sig_catch(self):
        return self.stat_list[33]

    def wait_channel(self):
        return self.stat_list[34]

    def swapped_pages(self):
        return self.stat_list[35]

    def child_swapped_pages(self):
        return self.stat_list[36]

    def exit_signal(self):
        return self.stat_list[37]

    def last_processor(self):
        return self.stat_list[38]

    def real_time_priority(self):
        return self.stat_list[39]

    def policy(self):
        return self.stat_list[40]

    def io_blocks(self):
        return self.stat_list[41]

    def guest_time(self):
        return self.stat_list[42]

    def child_guest_time(self):
        return self.stat_list[43]

    def start_data(self):
        return self.stat_list[44]

    def end_data(self):
        return self.stat_list[45]

    def start_brk(self):
        return self.stat_list[46]

    def arg_start(self):
        return self.stat_list[47]

    def arg_end(self):
        return self.stat_list[48]

    def env_start(self):
        return self.stat_list[49]

    def env_end(self):
        return self.stat_list[50]

    def exit_code(self):
        return self.stat_list[51]
