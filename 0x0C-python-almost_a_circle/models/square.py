#!/usr/bin/python3
"""
Square.py: Defines the Square class.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """Print representation."""
        return ("[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size))
