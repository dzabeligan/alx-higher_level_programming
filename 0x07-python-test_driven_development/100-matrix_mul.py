#!/usr/bin/python3
"""Defines a matrix multiplication function."""


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
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for row_a in m_a:
        new_row = []
        for col_b in zip(*m_b):
            product = sum(a * b for a, b in zip(row_a, col_b))
            new_row.append(product)
        result.append(new_row)

    return result
