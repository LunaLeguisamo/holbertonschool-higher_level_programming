#!/usr/bin/python3

def no_c(my_string):
    len_s = len(my_string)
    new_s = ""
    for i in range(0, len_s):
        if my_string[i] == "C" or my_string[i] == "c":
            new_s += ""
        else:
            new_s += my_string[i]
    return new_s
