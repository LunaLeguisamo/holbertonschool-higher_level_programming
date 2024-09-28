#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This is a module
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle with inheritance of BaseGeometry class
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
