#!/usr/bin/python3
"""
This is a module
"""


class BaseGeometry:
    """
    Class with a method area
    """

    def area(self):
        
        """
        Method to calculate area
        """
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        
        """
        Method to validate if a number is an interger
        """
        
        self.name = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
