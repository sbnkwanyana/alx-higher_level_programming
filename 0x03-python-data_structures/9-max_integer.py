#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    index = 1
    if my_list is None or len(my_list) == 0:
        return None
    else:
        max = my_list[0]
        while index < len(my_list):
            if my_list[index] > max:
                max = my_list[index]
            index += 1
    return max
