#!/usr/bin/python3
"""
module contains function that returns a dictionary description of a class
"""


def class_to_json(obj):
    """
    function returns data dictionary of an class object
    """
    return obj.__doc__
