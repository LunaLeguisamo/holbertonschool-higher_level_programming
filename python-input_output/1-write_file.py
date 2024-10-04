#!/usr/bin/python3
"""
This module define a function that write a file
 and return the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write a file with the text and return the
     number of characters
    """

    with open(filename, "w") as myF:
        myF.write(text)

        return myF.write(text)
