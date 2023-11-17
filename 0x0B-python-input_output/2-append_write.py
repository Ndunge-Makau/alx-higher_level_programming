#!/usr/bin/python3
"""
2-append_write.py: Defines the append_write() function.

"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file."""
    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
