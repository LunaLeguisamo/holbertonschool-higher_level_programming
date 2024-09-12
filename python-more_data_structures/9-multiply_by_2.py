#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for clave, valor in a_dictionary.items():
        b_dictionary[clave] = valor * 2
    return b_dictionary
