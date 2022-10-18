#!/usr/bin/python3
"""
This is the "Add Integer"  module.
This module supplies one function, add_integer(),
which adds together 2 int or float types and returns an int.
"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as an integer.
    Otherwise raise a TypeError for given incorrect argument type.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
