#!/usr/bin/python3
"""
Reading n lines of a text file in UTF-8 format and printing to standard out.
"""


def write_file(filename="", text=""):
    """
    Opening a text file in UTF-8 format and writing in the file.
    Opening the file in read mode and returning the number of characters.
    """
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        return (my_file.write(text))
