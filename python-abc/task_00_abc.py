#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog (Animal):
    def sound(self):
        sound = "Bark"
        return "Bark"

class Cat(Animal):
    def sound(self):
        sound = "Meow"
        return "Meow"
