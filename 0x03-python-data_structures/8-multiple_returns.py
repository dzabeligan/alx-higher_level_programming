#!/usr/bin/python3
"""Task 8
    """


def multiple_returns(sentence):
    """return multiple values

    Args:
        sentence (string): sentence

    Returns:
        tuple: length, first character
    """
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
