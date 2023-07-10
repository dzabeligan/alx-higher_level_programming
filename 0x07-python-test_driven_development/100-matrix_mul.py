#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def validate_matrix(matrix, matrix_string='The matrix'):
    """
    Validates a matrix according to the requirements.

    Args:
        matrix (list): The matrix represented as a list of lists.

    Raises:
        TypeError: If the matrix is not a list or not a list of lists, or if
        one element of the matrix is not an integer or float, or if the matrix
        is not a rectangle.
        ValueError: If the matrix is empty.

    Returns:
        int: The number of columns in the matrix.
    """
    if not isinstance(matrix, list):
        raise TypeError(f"{matrix_string} must be a list")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{matrix_string} must be a list of lists")
    if not matrix or not matrix[0]:
        raise ValueError(f"{matrix_string} can't be empty")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            f"{matrix_string} should contain only integers or floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(
            f"each row of {matrix_string} must be of the same size")

    return len(matrix[0])


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list
        of lists, or if one element of m_a or m_b is not an integer or float,
        or if m_a or m_b is not a rectangle.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be
        multiplied.

    Returns:
        list: The resulting matrix after multiplying m_a and m_b.
    """
    cols_a = validate_matrix(m_a, 'm_a')
    _ = validate_matrix(m_b, 'm_b')

    if cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row_a in m_a:
        new_row = []
        for col_b in zip(*m_b):
            product = sum(a * b for a, b in zip(row_a, col_b))
            new_row.append(product)
        result.append(new_row)

    return result
