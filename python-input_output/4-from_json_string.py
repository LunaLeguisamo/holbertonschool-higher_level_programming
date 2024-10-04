#!/usr/bin/python3
"""
Module that define a function that returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Define a function that returns an object
    (Python data structure) represented by a JSON string
    """

    return json.loads(my_str)
