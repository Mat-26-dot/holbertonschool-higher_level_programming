#!/usr/bin/python3
"""Defines the same class"""

is_same_class = __import__('2-is_same_class').is_same_class
"""Import from this file to the main"""
def is_sameclass(obj, a_class):
    """Same class containing obj, & a_class""" 
    return type(obj) is a_class
