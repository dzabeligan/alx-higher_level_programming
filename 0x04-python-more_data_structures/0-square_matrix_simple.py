#!/usr/bin/python3
"""Task 0"""


def square_matrix_simple(matrix=[]):
    """compute the square of numbers in matrix.

    Args:
        matrix (list, optional): matrix. Defaults to [].

    Returns:
        list: matrix of squares
    """
    return ([list(map(lambda x: x * x, row)) for row in matrix])
