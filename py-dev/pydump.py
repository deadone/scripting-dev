#!/usr/bin/python3
# Filename: pydump.py
# Author: dead1
# Details: HexDump

###########################################################
# command line usage example :   'python3 pydump.py test.exe'
###########################################################

import codecs
import sys
import os


class color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    end = '\033[0m'


def dump(file_name):
    the_file = open(file_name, "rb")
    file_string = the_file.read()
    hex_list = ['{:02x}'.format(b) for b in file_string]
    int_list = list(file_string)
    file_length = len(hex_list)
    combined_string = ""
    off_set = 0
    print(color.red, "*** Dead1's Hex Dump ***", color.end)
    for _ in hex_list:
        print(f"[{format(off_set, 'x').rjust(8, '0')}]", end="\t")
        for count in range(0, 16):
            if off_set == file_length:
                buff_count = 16 - count
                buffer = "   " * buff_count
                print(buffer, "\t", combined_string)
                print(color.green, "Total Length:", file_length, "bytes", color.end)
                exit()
            print(hex_list[off_set], end=" ")
            if 33 < int_list[off_set] < 126:
                combined_string += codecs.decode(hex_list[off_set], "hex").decode('ascii')
            else:
                combined_string += "."
            off_set += 1
        print("\t", combined_string)
        combined_string = ""


if len(sys.argv) == 2:
    file_name = sys.argv[1]
    if os.path.isfile(file_name):
        dump(file_name)
    else:
        print("File not found.\nCorrect Usage: 'python3 pydump.py shell.exe'")
        exit()
else:
    print("Error.\nCorrect Usage: 'python3 pydump.py shell.exe'")
    exit()
