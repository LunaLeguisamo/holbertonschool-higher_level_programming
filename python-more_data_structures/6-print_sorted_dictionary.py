#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for clave, valor in sorted(a_dictionary.items()):
        print("{:s}: {}" .format(clave, valor))
