#!/usr/bin/python3
"""Task 11
    """


def delete_at(my_list=[], idx=0):
    """delete item in list

    Args:
        my_list (list, optional): list. Defaults to [].
        idx (number): index

    Return: list with item deleted
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
