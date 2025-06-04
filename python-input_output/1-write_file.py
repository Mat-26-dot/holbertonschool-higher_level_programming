#!/usr/bin/python3
"""
This module provides a function to write a string to a text file
and return the number of characters written.
"""

def write_file(filename="", text=""):

    with open(filename, 'w') as f:
        chars_written = f.write("This School is so cool!\n")
        print(chars_written)
        return (text)