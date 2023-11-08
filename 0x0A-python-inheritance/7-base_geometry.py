#!/usr/bin/python3
"""
Deines the BaseGeometry class.

"""


class BaseGeometry:
    """Defines the BaseGeometry class."""
    def area(self):
        """raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
