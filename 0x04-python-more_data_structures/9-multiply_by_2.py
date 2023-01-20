#!/usr/bin/python3
"""Task 9"""


def multiply_by_2(a_dictionary):
    """Multiply all values in dictionary by 2

    Args:
        a_dictionary (Any): dictionary

    Returns:
        dictionary: Dictionary with values multiplied by 2
    """
    return {key: a_dictionary[key] * 2 for key in a_dictionary}
