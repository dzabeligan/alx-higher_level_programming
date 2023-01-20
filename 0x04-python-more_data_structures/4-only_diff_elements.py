#!/usr/bin/python3
"""Task 4"""


def only_diff_elements(set_1, set_2):
    """build set of elements exclusive to one of two sets

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: elements in only one set
    """
    return set_1 ^ set_2
