#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    if my_list is None or len(my_list) < 0:
        return my_list
    [unique_list.append(number) for number in my_list if number not in unique_list]
    return (sum(unique_list))

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
