#!/usr/bin/python3
"""
101-add_attribute.py: Defines the function add_attribute.

"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible."""
    if (hasattr(obj, "__dict__") is True):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
