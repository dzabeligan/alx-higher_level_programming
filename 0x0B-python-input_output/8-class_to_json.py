#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structures suitable for
    JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary with serializable attributes of the object.

    Raises:
        None

    Note:
        - The function uses the '__dict__' attribute of the object to access
        its instance variables.
        - The resulting dictionary can be directly serialized to JSON using the
        'json' module.

    Example:
        class MyClass:
            def __init__(self, name, age, data):
                self.name = name
                self.age = age
                self.data = data

        obj = MyClass("John", 30, {"key": "value"})

        json_dict = class_to_json(obj)
        print(json_dict)
    """
    return obj.__dict__
