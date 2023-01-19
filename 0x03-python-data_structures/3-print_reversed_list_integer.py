#!/usr/bin/python3
"""Task 3: Print reversed list integer
    """


def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer: Print list item in reverse

    Args:
        my_list (list, optional): list. Defaults to [].
    """
    if my_list:
        for num in reversed(my_list):
            print("{:d}".format(num))
