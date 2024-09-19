#!/usr/bin/python3

"""
This module defines a class Square.
"""


class Square:
    """
    An class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for i in position:
            if not isinstance(i, int) or i < 0:
                raise ValueError(
                    "position must be a tuple of 2 positive integers"
                    )
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for i in value:
            if not isinstance(i, int) or i < 0:
                raise ValueError(
                    "position must be a tuple of 2 positive integers"
                    )

        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
