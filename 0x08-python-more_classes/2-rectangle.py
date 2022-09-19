#!/usr/bin/python3
"""
This module contains the class definition for a rectangle
with a height and a width property
"""


class Rectangle:
    """
    Class definition of a rectangle with height and width
    """
    def __init__(self, width=0, height=0):
        """
        initialization function of the rectangle class

        Args:
            width - this sets the width of the rectangle
            height - this sets the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width property returns the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        height property returns the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        width setter sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        height setter sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates and returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates and returns the perimiter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
