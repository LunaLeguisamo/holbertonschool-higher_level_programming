#!/usr/bin/python3
"""
This module defines a class lookup.
"""
def lookup(obj):
    """
    Return a list of the attributes and methods of an object.
    """
    return dir(obj)
