#!/usr/bin/python3
"""
Module contains from_json_string function that
converts a json string to an python object
"""


import json


def from_json_string(my_str):
    """
    loads a string from json to a python object
    """
    return json.loads(my_str)
