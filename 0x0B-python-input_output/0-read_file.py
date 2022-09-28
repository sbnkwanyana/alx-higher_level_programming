#!/usr/bin/python3
"""
Module contains function read_file that reads a file.
"""


def read_file(filename=""):
    """
    read_file functions reads a given text file and prints out the output
    to the standard output
    """
    with open(filename, encoding="utf-8") as file:
        data = file.read()
    print(data, end="")
