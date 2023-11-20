#!/usr/bin/python3
"""
100-append_after.py: Defines the ppend_after() function.

"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string."""
    my_strings = ""

    with open(filename, 'r', encoding="utf-8") as my_file:
        for line in my_file:
            my_strings += line
            if search_string in line:
                my_strings += new_string

    with open(filename, 'w', encoding="utf-8") as my_file:
        my_file.write(my_strings)
