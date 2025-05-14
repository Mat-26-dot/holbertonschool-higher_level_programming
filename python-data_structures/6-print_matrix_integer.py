#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for list_of_row in matrix:
        if list_of_row: 
            for list_of_numbers in list_of_row[:-1]:  
                print("{:d}".format(list_of_numbers), end=" ")
            print(list_of_row[len(list_of_row) - 1])