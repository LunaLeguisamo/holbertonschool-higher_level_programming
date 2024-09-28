#!/usr/bin/python3

"""
This module defines a Rectangle class that inherits from BaseGeometry.
The Rectangle class represents a rectangle defined by its width and height,
both of which must be positive integers.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.

    """
    def __init__(self, width, height):
        """
        Initialize a new instance of Rectangle.

        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):

        """
        Method str that print
        """
        return ("[Rectangle] {:d}/{:d}" .format(self.__width, self.__height))
