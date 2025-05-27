#!/usr/bin/python3
"""Class defines rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height =0):
        """Initialize a new rectangle instance
        Args:
            width (int): The width of the rectangle (default 0)
            height (int): The height of a rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """Retrieve height of a rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return string representation of rectangle using '#' characters.
        Returns an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)
        return "\n".join(lines)
