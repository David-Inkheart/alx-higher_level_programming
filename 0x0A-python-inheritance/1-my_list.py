#!/usr/bin/python3
"""
Inheriting a list
"""


class MyList(list):

    def __init__(self):
        pass

    def print_sorted(self):
        """
        sorting a list.
        """
        print(sorted(self))
