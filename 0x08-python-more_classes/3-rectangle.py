#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

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

    def area(self):
        """Compute the area of the Rectangle.

        Returns:
            number: Area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the Rectangle.

        Returns:
            number: Perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        """Representation for the Rectangle class.

        Returns:
            str: Representation of the Rectangle class
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            _ = [rect.append('#') for _ in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
