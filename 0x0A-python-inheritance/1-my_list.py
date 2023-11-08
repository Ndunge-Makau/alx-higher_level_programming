#!/usr/bin/python3
"""
Defines the MyList class.

"""


class MyList(list):
    """
    Class MyList that inherits from list.
    """
    def print_sorted(self):
        """Prints sorted list"""
        return print((sorted(self)))
