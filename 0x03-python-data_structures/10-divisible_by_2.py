#!/usr/bin/python3
"""Task 10
    """


def divisible_by_2(my_list=[]):
    """return boolean list with value at index equal to number at same index in
    input list being even

    Args:
        my_list (list, optional): list. Defaults to [].
    """

    is_even = []
    for num in my_list:
        is_even.append(num % 2 == 0)

    return is_even
