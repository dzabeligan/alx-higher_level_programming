#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of size
    n.

    Args:
        n (int): The size of the Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.

    Raises:
        None
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
