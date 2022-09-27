#!/usr/bin/python3
"""
Module contains a funcion write_file that writes to a file
"""


def write_file(filename="", text=""):
    """
    write_file function writes to a text file and overrites the contents
    of an older file
    """
    with open(filename, encoding="UTF-8", mode="w") as file:
        return file.write(text)
