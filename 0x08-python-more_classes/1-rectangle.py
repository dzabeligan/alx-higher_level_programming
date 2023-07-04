#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, _width=0, _height=0):
        """Initializes a new Rectangle.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        self.width = _width
        self.height = _height

    @property
    def width(self):
        """Get the width of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
