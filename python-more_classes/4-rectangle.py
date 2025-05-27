#!/usr/bin/python3
"""Class that define rectangle"""



class Rectangle:
    """Defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        # Sets values for tgetter and setter
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter for the private attribute __width
        return self.__width

    @width.setter
    def width(self, value):
        # Setter for the private attribute __width
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Getter for the private attribute __height
        return self.__height

    @height.setter
    def height(self, value):
        # Setter for the private attribute __height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        # Returns the area of the rectangle (width * height)
        return self.width * self.height

    def perimeter(self):
        # Returns the perimeter of the rectangle (2 * (width + height))
        # If width or height is 0, perimeter is 0
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        # Returns a string representation for print() and str()
        # Rectangle is drawn with '#' character
        # If width or height is 0, returns an empty string
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)
        return "\n".join(lines)

    def __repr__(self):
        # Returns a string that can recreate the object using eval()
        return f"Rectangle({self.width}, {self.height})"
