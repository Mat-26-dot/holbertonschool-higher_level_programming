#!/usr/bin/env python3
"""Create a basic serialization module that adds the 
functionality to serialize a Python dictionary"""


import json

def serialize_and_save_to_file(data, filename):
    """serialize and save data to the specified file"""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        result = json.load(f)
        return result

