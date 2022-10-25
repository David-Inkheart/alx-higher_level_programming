#!/usr/bin/python3
"""
Reading a text file in UTF-8 format and prints to standard out.
"""


def read_file(filename=""):
    """
    opening text file and printing to standard out.
    """
    with open(filename, 'r', encoding="UTF-8") as my_file_0:
        print(my_file_0.read(), end="")
