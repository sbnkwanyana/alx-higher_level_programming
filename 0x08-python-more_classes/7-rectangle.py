#!/usr/bin/python3
"""
This module contains the class definition for a rectangle
with a height and a width property and number of instances class attribute
"""


class Rectangle:
    """
    Class definition of a rectangle with height and width
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialization function of the rectangle class
        and increments the number of instance class attribute

        Args:
            width - this sets the width of the rectangle
            height - this sets the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        returns the string representation of the rectangle
        in # accorinding to its width and height
        """
        rect_str = ""
        i = 0
        j = 0
        if self.__width == 0 or self.__height == 0:
            return rect_str
        while i < self.__height:
            while j < self.__width:
                rect_str += str(self.print_symbol)
                j += 1
            if i != self.__height - 1:
                rect_str += "\n"
            j = 0
            i += 1
        return rect_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle class
        that can be recreated using eval
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Rectangles deconstrcutor function prints message prior being deleted
        and decrements the number of instances attribute
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
