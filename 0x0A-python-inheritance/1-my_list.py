#!/usr/bin/python3
"""
Module contains a single class MyList that inherits from list and sorts a list
"""


class MyList(list):
    """
    class MyList inherits from list and contains a function names print_sorted
    that sorts the list of integers in ascending order using the
    builtin sorted function
    """
    def print_sorted(self):
        sorted(self)
