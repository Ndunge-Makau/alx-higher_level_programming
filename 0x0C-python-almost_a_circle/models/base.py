#!/usr/bin/python3
"""
models/base.py: Defines the Base class.

"""
import json


class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            with open("{}.json".format(cls.__name__), 'w') as my_file:
                my_file.write("[]")
        with open("{}.json".format(cls.__name__), 'w') as my_file:
            my_string = ""
            for i in list_objs:
                my_string += Base.to_json_string(i.to_dictionary())
            my_file.write(my_string)
