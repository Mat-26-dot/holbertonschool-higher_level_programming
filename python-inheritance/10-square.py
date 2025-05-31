#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle


class square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2



