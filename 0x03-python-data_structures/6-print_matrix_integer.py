#!/usr/bin/python3
"""Task 6
    """


def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer: Print matrix

    Args:
        matrix (list, optional): matrix. Defaults to [[]].
    """
    if not matrix:
        return
    for row in matrix:
        i = 1
        length = len(row)

        for cell in row:
            if i == length:
                print("{:d}".format(cell), end='')
            else:
                print("{:d}".format(cell), end=' ')
            i += 1
        print()
