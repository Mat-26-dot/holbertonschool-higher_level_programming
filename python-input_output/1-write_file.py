#!/usr/bin/python3

def write_file(filename="", text=""):

    with open(filename, 'w') as f:
        chars_written = f.write("This School is so cool!\n")
        print(chars_written)
        return (text)

