#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    modified_dictionary = a_dictionary.copy()
    for key, and_value in a_dictionary.items():
        if value == and_value:
            del modified_dictionary[key]
    return modified_dictionary
