#!/usr/bin/python3
"""
8-class_to_json.py: Defines the class_to_json() function.

"""
import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
