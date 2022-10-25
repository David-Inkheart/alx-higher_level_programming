#!/usr/bin/python3
"""
Writing an object to a text file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Opening and writing to file.
    """
    with open(filename, 'w', encoding="UTF-8") as my_file:
        json.dump(my_obj, my_file)
