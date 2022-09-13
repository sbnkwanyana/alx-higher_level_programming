#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    counter = 0
    new_list = []
    while counter < list_length:
        try:
            result = my_list_1[counter] / my_list_2[counter]
            new_list.append(result)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        finally:
            counter += 1
            continue
    return new_list
