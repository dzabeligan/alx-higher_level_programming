#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified
        class, False otherwise.
    """
    return isinstance(obj, a_class) and obj.__class__ is a_class
