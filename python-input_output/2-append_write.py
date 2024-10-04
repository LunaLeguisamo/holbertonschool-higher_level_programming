#!/usr/bin/python3
"""
This module define a function that appends a
string at the end of a text file
and return the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
     and return the number of characters added
    """

    with open(filename, "a") as f:
        return f.write(text)
