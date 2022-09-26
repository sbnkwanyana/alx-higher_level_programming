#!/usr/bin/python3
"""
This module contains the function is_kind_of_class that accepts
2 parameters where the first object parameter is used to check if its a
kind of the second class paramter
"""


def is_kind_of_class(obj, a_class):
    """
    function is_kind_of_class uses builtin fcuntion isinstance() function
    to determine if a given object is an kind of a specified class
    """
    return isinstance(obj, a_class)
