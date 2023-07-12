#!/usr/bin/python3
"""Defines a string-to-json function."""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of the provided object (string).

    Args:
        my_obj (str): The object (string) to be converted to JSON.

    Returns:
        str: The JSON representation of the object.

    Raises:
        None

    Note:
        - The function uses the 'json' module from the Python standard library
        for serialization.

    Example:
        my_obj = "Hello, world!"

        json_string = to_json_string(my_obj)
        print(json_string)
    """
    return json.dumps(my_obj)
