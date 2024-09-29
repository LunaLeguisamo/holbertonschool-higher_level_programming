#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("The radius value must be positive")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return (2 * math.pi) * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height values must be positives")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(Shape):
    area = Shape.area
    print("Area: {}" .format(Shape.area()))
    perimeter = Shape.perimeter()
    print("Perimeter: {}" .format(Shape.perimeter()))
