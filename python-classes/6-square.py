#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # Uses the size setter
        self.position = position  # Uses the position setter

    # PROPER INDENTATION: Properties at class level
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):  # Lowercase 'value' (Python convention)
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # VALIDATE FIRST before assignment
        if (not isinstance(value, tuple) or 
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Assign only if valid

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return  # CORRECT INDENTATION: inside the if-block
        
        # Vertical offset
        for _ in range(self.__position[1]):
            print()
        
        # Print square lines
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
