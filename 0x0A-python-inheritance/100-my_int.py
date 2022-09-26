#!/usr/bin/python3
"""
Module contains a MyInt class that inverts
the == and != operators
"""


class MyInt(int):
    """
    MyInt class overrides the magic functions eq and ne
    (equals to, not equals to) and inverts there functionality
    """

    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
