#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    value = number % 10
    print(value, end="")
    return (value)
