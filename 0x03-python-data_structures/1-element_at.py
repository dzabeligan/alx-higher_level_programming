#!/usr/bin/python3

def element_at(my_list, idx):
    """element_at: return element at index in list

    Args:
        my_list (Any): list
        idx (number): number

    Returns:
        Any | None: item at index or None if index is less than 0 or greater
        than list length
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
