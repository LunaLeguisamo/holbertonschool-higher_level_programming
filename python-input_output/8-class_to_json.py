#!/usr/bin/python3
"""
This module define a function that returns the
dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""

import json


def class_to_json(obj):
    """
    class with inheritance
    """

    return json.dumps(obj.__dict__)
