#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        type(self).number_of_instances += 1
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
        """Printable representation for the Rectangle class.

        Returns:
            str: Representation of the Rectangle class.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for i in range(self.__height):
            string += '#' * self.__width
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self) -> str:
        """Representation for the Rectangle class.

        Returns:
            str: Representation of the Rectangle class.
        """
        rect = "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Print a message when deleting a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
