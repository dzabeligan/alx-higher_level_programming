#!/usr/bin/python3
"""Defines a json-to-object function."""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by the provided JSON string.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.

    Raises:
        None

    Note:
        - The function uses the 'json' module from the Python standard library
        for deserialization.

    Example:
        my_str = '{"name": "John", "age": 30, "city": "New York"}'

        data_structure = from_json_string(my_str)
        print(data_structure)
    """
    return json.loads(my_str)
