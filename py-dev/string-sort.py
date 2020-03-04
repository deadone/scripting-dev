#!/usr/bin/python3
# Filename: string-sort
# Author: dead1
# Details: Random String Generator

######################################################
# command line usage example :   'python3 string-sort.py 500'
# command line find substring:   'python3 string-sort.py filename.txt substring'
# command line interface :       'python3 string-sort.py'
######################################################

import string
import os
from random import randint
import sys

file_name = "currentbuffer.txt"
dictionary = "1234567890" + string.ascii_letters
dictionary_length = len(dictionary)


class color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    end = '\033[0m'


def randomizer(check, dictionary_length):
    random_number = randint(0, dictionary_length - 1)
    if random_number == check:
        random_number = randint(0, dictionary_length - 1)
        if random_number == check:
            random_number = randint(0, dictionary_length - 1)
    return random_number


def random_string(string_size, dictionary, dictionary_length):
    random_string = ""
    check = 0
    for x in range(string_size):
        random_number = randomizer(check, dictionary_length)
        random_string += dictionary[random_number]
        check = random_number
    return random_string


def find_string(filename, string):
    if os.path.isfile(filename):
        location = 0
        the_file = open(filename, "r")
        file_string = the_file.read()
        if string in file_string:
            print("\nThe substring can be found beginning at offset:", color.red, color.bold, file_string.find(string),
                  color.end, "\n")
            exit()
        else:
            print(color.red, "\nString not found.", color.end)
            exit()
    else:
        print("File not found.\nCorrect Usage: 'python3 string-sort.py filename.txt substring'")
        exit()


def file_management(filename):
    print(color.blue, "\n *** [ File Management ] ***", color.end)
    keep = input("Did you want to keep a file_name containing the string? [y/n]: ")
    if keep == "y":
        print("File with string contained was saved as", color.red, filename, color.end)
    else:
        print("File", color.red, filename, color.end, " was deleted.")
        os.remove(filename)
    exit()


string_size = 0
if len(sys.argv) == 3:
    file_name = sys.argv[1]
    sub_string = sys.argv[2]
    find_string(file_name, sub_string)
else:
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        string_size = int(sys.argv[1])
        the_string = random_string(string_size, dictionary, dictionary_length)
        print(the_string)
        exit()
    else:
        print(color.blue, "*** [ Dead1's Random String Constructor / Pattern Analyzer v.1.0 ] ***", color.green)
        print("Command Line Usage Example :  'python3 string-sort.py 500'")
        print("Command Line Find Substring : 'python3 string-sort.py filename.txt substring'")
        print("Command Line Interface :      'python3 string-sort.py'", color.end)
        file_name = str(input("File Name to Use/Overwrite: "))
        if os.path.isfile(file_name):
            choice1 = input("File Exists. Did you want to search for a sub-string? [y/n]: ")
            if choice1 == "y":
                sub_string = input("Input the substring: ")
                find_string(file_name, sub_string)
            else:
                string_size = int(input("Input the length for a randomized string: "))
        else:
            string_size = int(input("Input the length for a randomized string: "))
            print()

print(color.blue, "*** [ Generated String ] ***", color.red)
the_string = random_string(string_size, dictionary, dictionary_length)
print(the_string)
the_file = open(file_name, "w+")
the_file.write(the_string)
the_file = open(file_name, "r")
file_string = the_file.read()
print(color.blue, "\n *** [ Substring Parsing ] ***", color.end)
choice = input("Do you want to find the offset of a sub-string within the generated string? [y/n]: ")

if choice == 'y':
    subString = input("Please enter the sub-string to search for: ")
    if subString in file_string:
        offset = file_string.find(subString)
        print("\nThe sub-string can be found starting at offset:", color.red, offset, color.end)
        file_management(file_name)
    else:
        print(color.yellow, "\nThat string doesnt exist.\n", color.end)
        file_management(file_name)
else:
    file_management(file_name)
