#!/usr/bin/python3
"""
This is a module
"""


class BaseGeometry:
    """
    Class with a method area
    """

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = value
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
