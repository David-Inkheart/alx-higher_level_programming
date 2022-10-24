#!/usr/bin/python3
"""
Function returns True if the obj is an instance of an instance of a class.
"""


def is_kind_of_class(obj, a_class):

    """
    Function returning true if the instance obj is of type a_class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
