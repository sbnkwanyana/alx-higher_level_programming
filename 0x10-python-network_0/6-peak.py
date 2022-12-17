#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
    Prototype: def find_peak(list_of_integers):
"""

def find_peak(list_of_integers):
    """
    Function find_peak uses builtin max function to find the peak
    """
    if list_of_integers is None or list_of_integers == []:
        return None
    else:
        return max(list_of_integers)
