#!/usr/bin/python3
"""
This module contains a Base class for a geometry object
with non implemented function definition for calculating the area
"""


class BaseGeometry():
    """
    BaseGeometry contains a non implemented area function
    that throws and exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
