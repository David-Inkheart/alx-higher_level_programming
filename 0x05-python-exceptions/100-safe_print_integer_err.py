#!/usr/bin/python3
# 100-safe_print_integer_err.py


import sys


def safe_print_integer_err(value):
    """
    A function that prints an integer
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
