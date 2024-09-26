#!/usr/bin/python3
"""
This is a function that returns True if the object is
an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False