#!/usr/bin/python3
"""
This module defines a class MyList with inheritance of list.
"""


class MyList(list):
    """
    Print a list in ascending sort.
    """
    def print_sorted(self):
        self.sort()
        print(self)
