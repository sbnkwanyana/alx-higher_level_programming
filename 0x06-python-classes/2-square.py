#!/usr/bin/python3
"""
This module contains the square class
"""


class Square:
    """
    Class represents a square
    """
    def __init__(self, size=0):
        """
        initializes private instance attribute with provided size

        Args:
            size: must be a valid integer size greater or equal to zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
