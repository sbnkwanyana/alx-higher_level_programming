#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for key, and_value in a_dictionary.items():
        if value == and_value:
            key_list.append(key)
    for i in key_list:
        del a_dictionary[i]
    return a_dictionary
