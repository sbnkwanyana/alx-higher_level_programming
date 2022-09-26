#!/usr/bin/python3
"""
Module contains a square class that inherits from the imported geometery
module
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """
    Square class calculates the area of a square
    """
    def __init__(self, size):
        """
       function initializes the square by first validating the passed in
       size value

       args:
           size: the size of the sides of a square
       """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
       area function calculate the area of a square
        """
        return self.__size * self.__size

    def __str__(self):
        """
       returns a tring representing the square
       """
        return "[Square] {}/{}".format(self.__size, self.__size)
