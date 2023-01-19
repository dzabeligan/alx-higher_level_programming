#!/usr/bin/python3
"""Task 9
    """


def max_integer(my_list=[]):
    """return maximum integer in list

    Args:
        my_list (list, optional): list. Defaults to [].
    """
    if not my_list:
        return None

    max_n = float('-inf')
    for num in my_list:
        if num > max_n:
            max_n = num
    return max_n
