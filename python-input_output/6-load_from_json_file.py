#!/usr/bin/python3
"""
This module define a function that creates
an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """
    This module define a function that creates
    an Object from a “JSON file”:
    """
    with open(filename, "r") as f:
        return json.load(f)
