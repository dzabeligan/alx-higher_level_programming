#!/usr/bin/python3
"""Task 6"""


def print_sorted_dictionary(a_dictionary):
    """print sorted dictionary

    Args:
        a_dictionary (dictionary): dictionary
    """
    _ = [print(f"{k}: {a_dictionary[k]}") for k in sorted(a_dictionary)]
