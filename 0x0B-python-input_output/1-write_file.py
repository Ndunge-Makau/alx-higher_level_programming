#!/usr/bin/python3
"""
1-write_file.py: Defines the write_file() function.

"""


def write_file(filename="", text=""):
    """Writes text to files."""
    with open(filename, 'w', encoding="utf-8") as my_file:
        return my_file.write(text)
