#!/usr/bin/python3

def islower(c):
    valor = ord(c)
    if valor >= 97 and valor <= 122:
        return True
    else:
        return False


def uppercase(str):
    for a in str:
        if islower(a) is True:
            a = chr(ord(a) - 32)
        elif islower(a) is False:
            a = a
        print("{}" .format(a), end="")
    print()
