#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    key_a, value_a = list(a_dictionary.items())[0]

    for key, value in a_dictionary.items():
        if value > value_a:
            value_a = value
            key_a = key
    return key_a
