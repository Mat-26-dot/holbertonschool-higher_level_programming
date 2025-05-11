#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = sys.argv[1:]
int_args = map(int, args)
result = sum(map(int, args))
print(result)
