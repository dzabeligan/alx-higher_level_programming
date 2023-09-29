#!/usr/bin/python3
"""Implement find_peak"""


def find_peak_helper(list_of_integers, previous_number):
    """Recursive approach to find the peak value in a list of integers

    Args:
        list_of_integers (int[]): unsorted integer array
        previous_number (int): previous number

    Returns:
        int: first peak found
    """
    if len(list_of_integers) == 1:
        return max(list_of_integers[0], previous_number)
    if previous_number > list_of_integers[0]:
        return previous_number

    return find_peak_helper(list_of_integers[1:], list_of_integers[0])


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.
    Any peak found is an acceptable solution.

    Args:
        list_of_integers (int[]): unsorted integer array

    Returns:
        int: first peak found
    """
    if list_of_integers == []:
        return None

    return find_peak_helper(list_of_integers, list_of_integers[0])
