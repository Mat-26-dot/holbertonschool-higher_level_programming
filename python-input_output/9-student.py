#!/usr/bin/python3
"""Module that defines student by dict representation"""


class Student:
    """Class that defines a student attributes"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        student_dict = {
                        "first_name": self.first_name,
                        "last_name": self.last_name,
                        "age": self.age
                    }
        return student_dict
