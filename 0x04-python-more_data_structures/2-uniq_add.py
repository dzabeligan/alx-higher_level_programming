#!/usr/bin/python3
"""Task 2"""


def uniq_add(my_list=[]):
    """add unique numbers in list

    Args:
        my_list (list, optional): list. Defaults to [].

    Returns:
        number: sum of unique numbers in list
    """
    uniq_sum = 0
    for num in set(my_list):
        uniq_sum += num
    return uniq_sum
