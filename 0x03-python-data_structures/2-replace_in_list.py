#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace_in_list: replace item in list

    Args:
        my_list (Any): list
        idx (number): index
        element (Any): list element

    Returns:
        Any: list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
