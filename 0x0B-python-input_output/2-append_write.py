#!/usr/bin/python3
"""
Appending a string at the end of a text file in UTF-8 format
and returning the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appending the text at the end of the file while returning
    the character count of what was added.
    """
    with open(filename, mode="a", encoding="UTF-8") as my_file:
        return my_file.write(text)
