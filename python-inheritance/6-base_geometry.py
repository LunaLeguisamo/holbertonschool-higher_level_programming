#!/usr/bin/python3
"""
This is a module
"""  


class BaseGeometry:
    def area(self):
        try:
            self.area
        except:
        print("area() is not implemented")
