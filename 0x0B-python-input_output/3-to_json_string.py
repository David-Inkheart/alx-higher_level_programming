#!/usr/bin/python3
"""
Returning the JSON representation of a string object.
"""
import json


def to_json_string(my_obj):

    """
    json.dumps: Serialize obj to a JSON formatted str using a conversion table.
    """
    return (json.dumps(my_obj))
