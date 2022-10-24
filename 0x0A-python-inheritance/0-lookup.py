#!/usr/bin/python3
"""
Function that returns the list of availables
attributes and methods of an object
"""


def lookup(obj):
    """
    Returning list of available attributes.
    """
    return(dir(obj))
