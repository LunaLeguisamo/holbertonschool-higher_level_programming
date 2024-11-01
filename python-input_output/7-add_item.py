#!/usr/bin/python3
"""
This module define a function that creates
an Object from a “JSON file”:
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =  __import__('6-load_from_json_file').load_from_json_file

if not add_item:
    add_item = []

load_from_json_file(add_item)

with open(add_item, "w") as file:
    json.dumps(file)

add_item.append = sys.argv[1::]
