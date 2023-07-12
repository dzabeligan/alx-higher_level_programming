#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


def add_items_to_list_and_save(items, filename):
    """
    Adds the provided items to a Python list and saves them to a file in JSON
    format.

    If the file exists, the existing list in the file will be combined with the
    new items.

    Args:
        items (List[str]): The list of items to be added.
        filename (str): The name of the file to save the list.

    Returns:
        None

    Raises:
        None

    Note:
        - The function uses the 'save_to_json_file' and 'load_from_json_file'
        functions from the 'json_utils' module.

    Example:
        # Suppose the script is executed as: python add_items.py item1 item2
        # item3
        arguments = sys.argv[1:]
        add_items_to_list_and_save(arguments, "add_item.json")
    """
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        existing_list = load_from_json_file(filename)
        if isinstance(existing_list, list):
            items.extend(existing_list)
    except FileNotFoundError:
        items = []

    save_to_json_file(items, filename)


if __name__ == "__main__":
    add_items_to_list_and_save(sys.argv[1:], "add_item.json")
