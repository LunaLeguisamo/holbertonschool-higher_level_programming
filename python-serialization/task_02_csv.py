#!/usr/bin/python3
"""
Module that define a function

"""

import json
import csv


def convert_csv_to_json(csv_filename):
    data = {}
    try:
        with open(csv_filename, "r") as file:
            csv_f = csv.DictReader(file)

            for i in csv:
                data.append(i)

        json.dump(data)
        return True

    except EOFError:
        return False
