#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python object created from the JSON file.

    Raises:
        None

    Note:
        - The function uses the 'json' module from the Python standard library
        for deserialization.
        - The file is opened and closed automatically using the 'with'
        statement.

    Example:
        filename = "data.json"

        loaded_object = load_from_json_file(filename)
        print(loaded_object)
    """
    with open(filename, "r") as file:
        return json.load(file)
