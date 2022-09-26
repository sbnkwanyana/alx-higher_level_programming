#!/usr/bin/python3
"""
Module contains the function inherits_from that determines if a
given object inherits from a specified class
"""


def inherits_from(obj, a_class):
    """
    function inherits_from uses the builtin issubclass function to determine
    if a given object type is a subclass (directly or indirectly)
    of a given class
    """
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
