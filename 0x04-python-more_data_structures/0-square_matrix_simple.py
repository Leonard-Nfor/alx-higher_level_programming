#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        square_row = []
        for element in row:
            squared_element = element **2
            square_row.append(squared_element)
        new_matrix.append(square_row)
    return new_matrix
