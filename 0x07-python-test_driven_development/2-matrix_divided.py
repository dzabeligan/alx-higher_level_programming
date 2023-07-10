#!/usr/bin/python3
"""Defines an matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number by which all elements of the matrix will
        be divided.

    Returns:
        list of lists: The new matrix with elements divided by div and rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
        , or if each row of the matrix does not have the same size, or if div
        is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list)for row in matrix) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    num_cols = len(matrix[0])
    if not all(len(row) == num_cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of"
                    " integers/floats")
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
