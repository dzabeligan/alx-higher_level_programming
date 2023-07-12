#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout.

    Args:
        filename (str, optional): filename. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f_ptr:
        print(f_ptr.read(), end="")
