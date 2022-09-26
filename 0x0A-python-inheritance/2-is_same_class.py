#!/usr/bin/python3
"""
Module contains the function is_same_class that determines whether
a class is exactly and instance of another class
"""


def is_same_class(obj, a_class):
    """
    function is_same_class uses builtin type() function to determine obj type
    and compares it to a_class for equality and returns True or false
    """
    return type(obj) == a_class
