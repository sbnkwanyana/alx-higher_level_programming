#!/usr/bin/python3
"""
This module contains a function called lookup that returns
a list object of all the attributes and methods of a class
"""


def lookup(obj):
    """
    function lookup uses builtin dir() function to return a list
    of all attributes and functions of a class
    """
    return dir(obj)
