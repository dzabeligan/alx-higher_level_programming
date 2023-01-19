#!/usr/bin/python3
"""Task 4
    """


def new_in_list(my_list, idx, element):
    """new_in_list: replace item in list. Original list is not mutated

    Args:
        my_list (Any): list
        idx (number): index
        element (Any): list item

    Returns:
        Any: list copy
    """
    copy = my_list.copy()

    if 0 <= idx < len(my_list):
        copy[idx] = element
    return copy
