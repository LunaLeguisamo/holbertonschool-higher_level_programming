#!/usr/bin/python3

for n in range(0, 10):
    for i in range(n + 1, 10):
        print("{}{}" .format(n,i), end=", ")
        if n == 8 and i == 9:
            print("{}{}" .format(n,i))
