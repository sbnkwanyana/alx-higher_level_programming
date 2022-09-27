#!/usr/bin/python3
"""
Module contains a funtion load_from_json_file that reads a file
and returns an python object
"""


import json


def load_from_json_file(filename):
    """
    load_from_json_file reads a file and converts the data to a python object
    """
    with open(file=filename, encoding="utf-8") as file:
        return json.loads(file.read())
