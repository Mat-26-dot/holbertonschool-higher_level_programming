#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
# Use map to square each element in each row, then convert to list
    return (list(map(lambda x: x **2, row)) for row in matrix)
