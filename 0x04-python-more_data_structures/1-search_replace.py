#!/usr/bin/python3
"""Task 1"""


def search_replace(my_list, search, replace):
    """search and replace items in list that match a search query

    Args:
        my_list (Any): list
        search (Any): search query
        replace (Any): replacement

    Returns:
        list(Any): list copy with replaced item
    """
    new_list = my_list[:]
    for i, elem in enumerate(new_list):
        if elem == search:
            new_list[i] = replace
    return new_list
