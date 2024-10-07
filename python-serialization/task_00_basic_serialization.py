#!/usr/bin/python3
"""
Module that define two functions that

"""

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data)


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        f = json.load(file)
        return f