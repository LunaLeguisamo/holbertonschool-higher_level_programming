#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix[0:]:
        for i in range(len(list)):
            if i < len(list) - 1:
                print("{:d} " .format(list[i]), end="")
            else:
                print("{:d}" .format(list[i]), end="")
        print()
