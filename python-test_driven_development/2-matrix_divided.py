#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a given divisor.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix is a list of lists of int/float
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows are the same size
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide and round
    return [[round(num / div, 2) for num in row] for row in matrix]
