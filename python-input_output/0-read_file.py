#!/usr/bin/python3

"""
Este módulo proporciona una función para leer el contenido de un archivo y
imprimirlo en la consola.
"""


def read_file(filename=""):
    """
    Lee el contenido del archivo especificado y lo imprime en la consola.
    """

    with open(filename, "r") as myFile:
        print(myFile.read(), end="")
