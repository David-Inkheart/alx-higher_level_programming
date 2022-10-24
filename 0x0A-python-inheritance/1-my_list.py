#!/usr/bin/python3
"""
Inherting from a list
"""


class MyList(list):

    def print_sorted(self):
        """
        sorting a list.
        """
        print (sorted(self))
