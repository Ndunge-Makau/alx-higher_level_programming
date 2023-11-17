#!/usr/bin/python3
"""
6-load_from_json_file.py: Defines the load_from_json_file() function.

"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file"""
    with open(filename, 'r', encoding="utf-8") as my_file:
        return json.load(my_file)
