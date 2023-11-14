#!/usr/bin/python3
"""
The Square class.

"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """The square class."""
    def __init__(self, size):
        self.integer_validator("size", size)

        Rectangle.__init__(self, size, size)
        self.__size = size
