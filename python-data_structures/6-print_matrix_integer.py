#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix[0:]:
        for i in range(0, len(matrix[0])):
            print("{:d} " .format(list[i]), end="")
        print()
