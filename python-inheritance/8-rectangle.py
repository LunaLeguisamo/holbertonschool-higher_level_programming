#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This is a module
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle that represents a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Validates the width and height using the integer_validator
        method from BaseGeometry.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
