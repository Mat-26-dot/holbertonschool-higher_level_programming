#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    args = sys.argv[1:]      # Get all command-line arguments except the script name
    
    int_args = map(int, args)  # Convert each argument to an integer
    result = sum(int_args)     # Sum all the integers
    print(result)              # Print the resulti
