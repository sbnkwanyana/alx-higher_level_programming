#!/usr/bin/python3
def print_last_digit(number):
    if number is not int or number is not float:
        return
    if number < 0:
        number = number * -1
    value = number % 10
    print(value, end="")
    return (value)
