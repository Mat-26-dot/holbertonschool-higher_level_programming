#!/usr/bin/python3
"""Module that defines student by dict representation"""
class Student:
    """Class that defines a student attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        #testing
        print("Student Details:")
        print("First_name:", first_name)
        print("Last_name:", last_name)
        print("Age:", age)

    def to_json(self, attrs=None):

        student_dict = {
                        "first_name": self.first_name,
                        "last_name": self.last_name,
                        "age": self.age,
                        }

        #testing
        return student_dict

