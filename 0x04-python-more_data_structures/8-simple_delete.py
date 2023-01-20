#!/usr/bin/python3
"""Task 8"""


def simple_delete(a_dictionary, key=""):
    """Delete key value in dictionary

    Args:
        a_dictionary (Any): dictionary
        key (str, optional): key. Defaults to "".

    Returns:
        dictionary: dictionary with deletedd key value pair
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
