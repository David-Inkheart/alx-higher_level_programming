#!/usr/bin/python3
"""
This is the "Say My Name" module.
The Say My Name module takes one required parameter and one optional.
It prints "My name is (first) (last)" where (first) and (last) are the args.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is (first) (last) if given, else print error.
    """
    if type(first_name) != str:
        raise TypeError("first name must be a string")
    if type(last_name) != str:
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
