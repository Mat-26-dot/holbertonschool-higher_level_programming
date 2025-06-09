#!/usr/bin/python3

class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print("Student Details:")
        print("First_name:", first_name)
        print("Last_name:", last_name)
        print("Age:", age)

    def to_json(self, attrs=None):

        student_dict = {
                        "first_name", self.first_name,
                        "last_name", self.last_name,
                        "age", self.age,

        }

        
        print("Attribute Names", attrs)
        student = Student("John", "Doe", 23)
        student.to_json

        return student_dict