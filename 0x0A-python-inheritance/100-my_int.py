#!/usr/bin/python3
"""
100-my_int.py: Defines the MyInt class.

"""


class MyInt(int):
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        """Defines behavior for the equality operator, =="""
        return self.number != other

    def __ne__(self, other):
        """Defines behavior for the inequality operator, !="""
        return self.number == other
