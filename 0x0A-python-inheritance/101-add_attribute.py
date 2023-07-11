#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute is to be added.
        attr_name (str): The name of the attribute.
        attr_value: The value of the attribute to be added.

    Raises:
        TypeError: If the object can't have a new attribute.

    Returns:
        None
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
