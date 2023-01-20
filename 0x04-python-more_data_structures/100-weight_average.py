#!/usr/bin/python3
"""Task 100"""


def weight_average(my_list=[]):
    """compute weighted average of entry in list

    Args:
        my_list (list, optional): entry list. Defaults to [].

    Returns:
        number: computed weighted average
    """
    if not isinstance(my_list, list) or not my_list:
        return 0

    total = 0
    freq = 0
    for entry in my_list:
        total += entry[0] * entry[1]
        freq += entry[1]
    return total/freq
