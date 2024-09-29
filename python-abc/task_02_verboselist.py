#!/usr/bin/env python3

from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list." .format(item))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list." .format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items." .format(len(item)))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list." .format(item))
        return item
