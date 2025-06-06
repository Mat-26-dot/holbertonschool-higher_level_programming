#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print("Area: {:.1f}".format(shape.area()))
    print("Perimeter: {:.1f}".format(shape.perimeter()))    

circle = Circle(5)
rectangle = Rectangle(4, 6)

shape_info(circle)
shape_info(rectangle)


