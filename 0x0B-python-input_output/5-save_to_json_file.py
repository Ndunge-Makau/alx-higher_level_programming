#!/usr/bin/python3
"""
5-save_to_json_file.py: Defines the save_to_json_file() function.

"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding="utf-8") as my_file:
        my_object = json.dumps(my_obj)
        my_file.write(my_object)
