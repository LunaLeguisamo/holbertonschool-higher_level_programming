#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix[0:]:
        for each in list[0:]:
            print("{:d} " .format(each), end="")
        print()
