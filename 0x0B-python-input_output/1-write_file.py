#!/usr/bin/python3
"""Writes content of text into a file."""


def write_file(filename="", text=""):
    """
    Writes the provided text to a file in UTF-8 encoding and returns the number
    of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The content to be written to the file.

    Returns:
        int: The number of characters written to the file. Returns 0 if an error
        occurs.

    Raises:
        None

    Note:
        - The function creates the file if it doesn't exist.
        - The function overwrites the content of the file if it already exists.
        - The function uses the 'with' statement to ensure the file is properly
        closed.

    Example:
        filename = "example.txt"
        text = "Hello, world!"

        characters_written = write_file(filename, text)
        print(f"Number of characters written: {characters_written}")
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
