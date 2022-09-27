#!/usr/bin/python3
"""
Module contains the append_file function that appends to a given text file
"""


def append_file(filename="", text=""):
    """
    append_file appends to a given text file and returns
    the number of characters printed
    """
    with open(file=filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
