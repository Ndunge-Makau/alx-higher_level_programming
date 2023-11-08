#!/usr/bin/python3
"""
Defines the inherits_from module.

"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
