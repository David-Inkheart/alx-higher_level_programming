#!/usr/bin/python3
"""
Returning a Python Data Structure represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    json.loads: Deserializes a string to a Python object using
    a conversion table.
    """
    return (json.loads(my_str))
