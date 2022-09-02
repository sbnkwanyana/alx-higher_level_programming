#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) == 0:
        return matrix
    square_matrix = []
    elements = 0
    while elements < len(matrix):
        square_matrix.append(matrix[elements].copy())
        elements += 1
    outer_index = 0
    for outer_list in matrix:
        inner_index = 0
        for inner_list_value in outer_list:
            square_matrix[outer_index][inner_index] = inner_list_value ** 2
            inner_index += 1
        outer_index += 1
    return square_matrix
