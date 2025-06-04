#!/usr/bin/python3
    # reads a text file 
def read_file(filename=""):
    # function reads a text file (UTF8) and prints to stdout
    with open(filename, encoding="UTF-8") as f:
        print(f.read())
