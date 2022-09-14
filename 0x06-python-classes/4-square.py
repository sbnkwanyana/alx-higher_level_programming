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

    def area(self):
        """
        function returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter property for size
       """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for size.

       Args:
           value - sets size equal to value
       """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
