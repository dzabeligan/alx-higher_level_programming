#!/usr/bin/python3
"""Implement find_peak"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.
    Any peak found is an acceptable solution.

    Args:
        list_of_integers (int[]): unsorted integer array

    Returns:
        int: first peak found
    """
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if the middle element is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the mid element is greater than the next element,
            # it's a peak; search the left half
            right = mid
        else:
            # If the mid element is less than or equal to the next element,
            # it's not a peak; search the right half
            left = mid + 1

    # The peak is found when left and right converge
    return list_of_integers[left]
