#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    else:
        index = 0
        new_list = []
        while index < len(my_list):
            if my_list[index] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
            index += 1
        return new_list
