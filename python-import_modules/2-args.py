#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    num_args = len(sys.argv) - 1
    
    if num_args == 0:
        print(f"Number of argument(s).")

    elif num_args == 1:
        print(f"Number of argument(s): 1 argument:")

    else:
        print(f"Number of argument(s): {num_args} arguments:")
