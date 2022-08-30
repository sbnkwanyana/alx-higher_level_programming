#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 1
        for value in row:
            print("{}".format(value), end="")
            if index != len(row):
                print(" ", end="")
            index += 1
        print("$")
