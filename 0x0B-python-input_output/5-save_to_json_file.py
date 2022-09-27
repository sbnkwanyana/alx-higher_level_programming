#!/usr/bin/python3
"""
Module contains save_to_file function that converts and object to json
then saves data to file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file serializes a json object and saves the result
    to a file
    """
    with open(file=filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
