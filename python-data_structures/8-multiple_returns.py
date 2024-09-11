#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        a = "None"
        b = 0
        tupla = (b, a)
    else:
        a = sentence[0]
        b = len(sentence)
        tupla = (b, a)
    return tupla
