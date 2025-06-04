#!/usr/bin/python3
"""
This module provides a function to write a string to a text file
and return the number of characters written.
"""

def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, 'w') as f:
        f.write(text)
        return (text)