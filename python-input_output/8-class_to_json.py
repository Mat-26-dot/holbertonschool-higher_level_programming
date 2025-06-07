#!/usr/bin/python3
"""
    Returns a dictionary of all instance attributes of obj.
    """


def class_to_json(obj):
    return obj.__dict__
