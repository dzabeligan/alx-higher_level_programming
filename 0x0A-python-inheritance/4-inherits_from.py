#!/usr/bin/python3
"""Defines a inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited
        from the specified class, False otherwise.
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class) and obj.__class__ is not a_class
