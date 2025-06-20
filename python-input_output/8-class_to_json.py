#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """
    Returns a dictionary of all instance attributes of obj.
    """
    return obj.__dict__
