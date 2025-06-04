#!/usr/bin/python3
    # function reads a text file (UTF8) and prints to stdout
def read_file(filename=""):
    # Reads a txt file
    with open(filename, encoding="UTF-8") as f:
        print(f.read())
