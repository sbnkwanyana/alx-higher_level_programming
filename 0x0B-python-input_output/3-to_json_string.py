#!/usr/bin/python3
"""
Module contains a to_json_string function that serializes an obect to json
"""


import json


def to_json_string(my_obj):
    """
    returns a json serialized data of an object
    """
    return json.dumps(my_obj)
