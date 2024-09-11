#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        i = 0
        for number in my_list[0:]:
            if number > i:
                i = number
    return i
