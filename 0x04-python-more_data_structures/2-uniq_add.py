#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    if my_list is None or len(my_list) < 0:
        return my_list
    [unique.append(number) for number in my_list if number not in unique]
    return (sum(unique))
