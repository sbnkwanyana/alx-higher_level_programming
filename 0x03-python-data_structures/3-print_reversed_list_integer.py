#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = my_list.sort(reverse=True)
    for i in my_list:
        print("{:d}".format(i))

print_reversed_list_integer([1, 2, 3, 4])