#!/usr/bin/python3
"""Module that defines student by dict representation"""


class Student:
    """Class that defines a student attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        student_dict = self.__dict__.copy ()
        if isinstance(attrs, list) and all (isinstance(attr, str)
        for attr in attrs):
            student_dict = {key: student_dict[key] for key in attrs if key
        in student_dict}

        return student_dict
