#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width  # Initialised for setter & getter
        self.height = height  # Initialised for setter & getter
        number_of_instances = 0
        print_symbol = "#"
        Rectangle.number_of_instances += 1

    @property
    def width(self):
            return self.__width # retrieving width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
                raise TypeError("width must be an integer")
        if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height # retrieve height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0    # handling edge cases if perimeter 0
        return 2 * (self.width + self.height) # otherwise return

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""   # handling an empty string (edge cases)

        row = str(self.print_symbol) * self.width
        return "\n".join([row for _ in range(self.height)])

    def __repr__(self):
            return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
