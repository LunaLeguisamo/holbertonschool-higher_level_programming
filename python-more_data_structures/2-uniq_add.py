#!/usr/bin/python3

def uniq_add(my_list=[]):
    n_list = []
    for i in my_list[0:]:
        if i not in n_list:
            n_list.append(i)
    return sum(n_list)
