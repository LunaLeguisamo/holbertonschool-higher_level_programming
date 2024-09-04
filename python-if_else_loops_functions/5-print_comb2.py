#!/usr/bin/python3

for n in range(0, 100):
    if n == 99:
        print("{}" .format(n))
    elif n <= 9:
        print("0{}" .format(n), end=", ")
    else:
        print("{}" .format(n), end=", ")
