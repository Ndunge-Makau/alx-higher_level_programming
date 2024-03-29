#!/usr/bin/python3
"""
10-student.py: Deines the Student class.

"""


class Student:
    """Defiens a Student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        my_dict = {}
        if isinstance(attrs, list):
            for i in attrs:
                if isinstance(i, str):
                    if i in self.__dict__:
                        my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__
