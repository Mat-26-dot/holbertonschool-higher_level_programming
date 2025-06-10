#!/usr/bin/python3
"""A module that defines a student"""


class Student:
    """A class that defines a student"""
    
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {k: self.__dict__[k] for k in attrs
                    if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
