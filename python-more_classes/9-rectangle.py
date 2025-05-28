#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle with width and height.
    Tracks the number of instances and allows custom print symbols.
    """

    # Public class attribute: tracks the number of Rectangle instances
    number_of_instances = 0

    # Public class attribute: symbol used for string representation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        width and height are optional and default to 0.
        """
        self.width = width   # Use property setter for validation
        self.height = height # Use property setter for validation
        Rectangle.number_of_instances += 1  # Increment instance counter

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        Must be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Enforce type
        if value < 0:
            raise ValueError("width must be >= 0")       # Enforce non-negative
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Must be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Enforce type
        if value < 0:
            raise ValueError("height must be >= 0")       # Enforce non-negative
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle.
        Area = width * height.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print_symbol.
        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        # Build each row as a string, then join with newlines
        row = str(self.print_symbol) * self.width
        return "\n".join([row for _ in range(self.height)])

    def __repr__(self):
        """
        Return a string that can recreate the rectangle using eval().
        Example: Rectangle(3, 4)
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called when an instance is deleted.
        Prints a goodbye message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.
        If equal, return rect_1.
        Both arguments must be Rectangle instances.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance with width == height == size.
        """
        return cls(size, size)
