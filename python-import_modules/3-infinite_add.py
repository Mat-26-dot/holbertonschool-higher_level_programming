#!/usr/bin/python3
import sys

args = sys.argv[1:]
print(args)

str_nums = ['0']
int_nums = map(int, str_nums)
print(list(int_nums))

str_nums = ['79' '10' '89']
int_nums = map(int, str_nums)
print(list(int_nums))
