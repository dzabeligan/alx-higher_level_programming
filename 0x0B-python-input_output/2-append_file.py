"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """
    Appends the provided text to a file in UTF-8 encoding and returns the
    number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The content to be appended to the file.

    Returns:
        int: The number of characters added to the file. Returns 0 if an error
        occurs.

    Raises:
        None

    Note:
        - If the file doesn't exist, it will be created.
        - The function uses the 'with' statement to ensure the file is properly
        closed.

    Example:
        filename = "example.txt"
        text = "Appended text"

        characters_added = append_write(filename, text)
        print(f"Number of characters added: {characters_added}")
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
