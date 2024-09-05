#!/usr/bin/env python3

def print_last_digit(number):
    if number < 0:
        number = -number
    else:
        number = number
    last = number % 10
    print("{}" .format(last), end="")
