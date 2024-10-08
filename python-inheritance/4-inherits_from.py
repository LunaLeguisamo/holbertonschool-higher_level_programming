#!/usr/bin/python3
"""
This is a function that returns True if the object is
an instance of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that
    inherited (directly or indirectly)
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
