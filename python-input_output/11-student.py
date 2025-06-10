#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print("first name:", first_name)
        print("last name", last_name)
        print("age:", age)

    def to_json(self, attrs=None):
        student_dict = self.__dict__
        
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
        return self._dict
