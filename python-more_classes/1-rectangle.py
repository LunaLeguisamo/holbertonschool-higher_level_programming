#!/usr/bin/python3

"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    An class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            TypeError("height must be an integer")
        if height < 0:
            ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            TypeError("width must be an integer")
        if width < 0:
            ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value
