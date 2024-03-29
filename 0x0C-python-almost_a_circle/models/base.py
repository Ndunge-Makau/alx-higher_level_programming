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
        else:
            with open("{}.json".format(cls.__name__), 'w') as my_file:
                my_list = []
                my_list.extend(i.to_dictionary() for i in list_objs)
                my_file.write(Base.to_json_string(my_list))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        my_list = []
        if json_string is None or "":
            return my_list
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Square":
            my_dummy = cls(12)
        else:
            my_dummy = cls(12, 2)
        my_dummy.update(**dictionary)
        return my_dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open("{}.json".format(cls.__name__), 'r') as my_file:
                my_list = Base.from_json_string(my_file.read())
                instance_list = []
                for i in my_list:
                    instance_list.append(cls.create(**i))
                return instance_list
        except FileNotFoundError:
            return []
