#!/usr/bin/python3
"""
Function returns True if object is an instance of
a class which inherited the specified class.
"""


def inherits_from(obj, a_class):

    """
    Return True only if the instance inherited a specific class
    """
    if issubclass(type(obj), a_class) and a_class is not type(obj):
            return True
    else:
        return False
