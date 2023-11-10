#!/usr/bin/python3
"""
Defines the text_indentation module

"""


def text_indentation(text):
    """
     prints a text with 2 new lines after each of these characters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if (text[i] in ".?:"):
            print(text[i], end="\n\n")
        else:
            if (text[i - 1] in ".?: ") and i != 0 and text[i] == ' ':
                continue
            print(text[i], end="")
