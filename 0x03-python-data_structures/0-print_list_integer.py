#!/usr/bin/python3

"""Print list of integers"""


def print_list_integer(my_list=[]):
    """print_list_integer prints integers in passed list

    Args:
        my_list (list, optional): list. Defaults to [].
    """
    for i in my_list:
        print("{:d}".format(i))
