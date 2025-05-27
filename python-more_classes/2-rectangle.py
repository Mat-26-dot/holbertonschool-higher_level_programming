#!/usr/bin/python3
"""Defines a rectangle by its height and width"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width      # Calls the width setter
        self.height = height    # Calls the height setter

    @property
    def width(self):
        """Get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle. Must be an integer >= 0.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle. Must be an integer >= 0.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the recytangle
        if width and height is 0, returns 0"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
