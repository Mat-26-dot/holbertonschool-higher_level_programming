#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        if not row:
            print()
        else:
            for column in row:  
                print("{:d}".format(column), end=' '
            if column != row[-1] else '\n')
        