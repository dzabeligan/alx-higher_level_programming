#!/usr/bin/python3
"""Task 5
    """


def no_c(my_string):
    """no_c: return string without `c` or `C`

    Args:
        my_string (string): string

    Returns:
        string: string without `c` or `C`
    """
    new_str = ""
    for char in my_string:
        if char not in "Cc":
            new_str += char

    return new_str
