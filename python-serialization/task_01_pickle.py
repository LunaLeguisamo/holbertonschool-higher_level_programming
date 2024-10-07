#!/usr/bin/python3
"""
Module that define a class

"""

import pickle


class CustomObject:

    def __init__(self, name=str, age=int, is_student=bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)

        except EOFError:
            raise ("Ran out of input")
        return None

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
