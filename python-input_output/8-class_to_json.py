#!/usr/bin/python3


def class_to_json(obj):
    """
    Returns a dictionary of all instance attributes of obj.
    """
    return obj.__dict__
