#!/usr/bin/python3
"""Task 1"""


def safe_print_integer(value):
    """Print an integer.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print(f"{value:d}")
        return (True)
    except (TypeError, ValueError):
        return (False)
