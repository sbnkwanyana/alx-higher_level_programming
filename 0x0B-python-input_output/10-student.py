#!/usr/bin/python3
"""
Module contains a student class that with two functions
init and to_json
"""


class Student():
    """
    Represents a student
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization function

        args:
            first_name: represents the students name
            last_name: represents the students surname
            age: represents the students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        """
        returns the dictionary dictionary representation of current object
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
