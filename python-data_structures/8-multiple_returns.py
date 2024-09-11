#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        a = None
        b = 0
    else:
        a = sentence[0]
        b = len(sentence)
        tupla = (b, a)
        return tupla
