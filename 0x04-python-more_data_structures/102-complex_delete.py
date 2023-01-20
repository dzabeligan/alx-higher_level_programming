#!/usr/bin/python3
"""Task 102"""


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): dictionary
        value (Any): value to delete

    Returns:
        dictionary: dictionary with value deleted
    """
    while value in a_dictionary.values():
        for k, val in a_dictionary.items():
            if val == value:
                del a_dictionary[k]
                break

    return a_dictionary
