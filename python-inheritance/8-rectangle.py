#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module defines a Rectangle class that inherits from BaseGeometry.
The Rectangle class represents a rectangle defined by its width and height,
both of which must be positive integers.
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.

    This class represents a rectangle and includes validation for its width
    and height. The rectangle is initialized with a specific width and height,
    which must be positive integers. The class leverages the integer_validator
    method from the BaseGeometry class to ensure the integrity of these values.

    Attributes:
        __width (int): The width of the rectangle. It must be a
        positive integer.
        __height (int): The height of the rectangle. It must also
        be a positive integer.
    """
    def __init__(self, width, height):
        """
        Initialize a new instance of Rectangle.

        The constructor accepts two parameters, width and height, which are
        validated using the integer_validator method from the BaseGeometry
        class.
        If the validation fails, appropriate exceptions are raised.

        Args:
            width (int): The width of the rectangle. Must be a positive
            integer.
            height (int): The height of the rectangle. Must be a positive
            integer.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or
            equal to zero.

        Example:
            >>> r = Rectangle(3, 5)
            >>> print(r)
            <Rectangle object at ...>
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
