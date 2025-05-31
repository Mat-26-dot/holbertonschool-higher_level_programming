#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle


class square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        """Initializes a Rectangle with validated width"""   
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
       """Returns the area of the Square"""
       return self.__size ** 2



