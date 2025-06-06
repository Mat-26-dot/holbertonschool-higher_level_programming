#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")

    elif num_args == 1:
        print("1 argument:")

    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")
