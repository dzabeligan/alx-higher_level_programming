#!/usr/bin/python3
"""Task 10"""


def best_score(a_dictionary):
    """return key with biggest integer value

    Args:
        a_dictionary (integer): dictionary

    Returns:
        str: key with biggest integer value
    """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, value in a_dictionary.items():
        if value > big:
            big = value
            ret = k
    return ret
