#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Defines a text file-reading function.

    Args:
        filename (str, optional): filename. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f_ptr:
        print(f_ptr.read(), end="")
