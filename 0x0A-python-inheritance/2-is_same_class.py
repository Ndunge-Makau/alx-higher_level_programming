#!/usr/bin/python3
"""
Defines the is_same_class module.

"""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of the specified class"""
    return True if type(obj) is a_class else False
