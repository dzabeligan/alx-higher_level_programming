#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes the provided object to a text file using its JSON representation.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None

    Raises:
        None

    Note:
        - The function uses the 'json' module from the Python standard library
        for serialization.
        - The file is opened in write mode ('w') and closed automatically using
        the 'with' statement.

    Example:
        my_obj = {"name": "John", "age": 30, "city": "New York"}
        filename = "data.json"

        save_to_json_file(my_obj, filename)
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
