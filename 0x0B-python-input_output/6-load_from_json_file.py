#!/usr/bin/python3
"""
Creating an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    open the file in read only and UTF-8 format.
    json.load: Deserializes the file to a
    Python object using a conversion table.
    """
    with open(filename, 'r', encoding="UTF-8") as my_file:
        return(json.load(my_file))
