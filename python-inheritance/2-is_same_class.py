#!/usr/bin/python3
"""Check if an object is exactly an instance"""


def is_sameclass(obj, a_class):
    """Validation""" 
    return type(obj) is a_class
