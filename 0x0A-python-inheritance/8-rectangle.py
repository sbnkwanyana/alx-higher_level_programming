#!/usr/bin/python3
"""
Module imports the base geometry class from module 7-base_geometry
and contains a rectangle class the inherits from baseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class contains an initialization function that validates
    the given width and height parameters using the inherited
    integer_validator function and sets the private width and height attributes
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
