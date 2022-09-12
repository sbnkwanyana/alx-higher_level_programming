#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    printed = 0
    while counter < x:
        try:
            print("{:d}".format(int(my_list[counter])), end="")
            counter += 1
            printed += 1
        except (ValueError, TypeError):
            counter += 1
            continue
    print("")
    return printed
