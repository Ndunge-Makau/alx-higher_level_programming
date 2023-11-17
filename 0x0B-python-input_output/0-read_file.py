#!/usr/bin/python3
"""
The 0-read_file.py module: read_file() function.

"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
