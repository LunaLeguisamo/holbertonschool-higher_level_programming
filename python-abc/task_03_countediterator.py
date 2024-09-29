#!/usr/bin/env python3

from abc import ABC, abstractmethod


class CountedIterator:
    def __init__(self, iterator, counter=0):
        self.counter = counter
        self.iterator = iter(iterator)

    def get_count(self):
        return self.counter

    def __next__(self):
        value = next(self.iterator)
        self.counter += 1
        return value
