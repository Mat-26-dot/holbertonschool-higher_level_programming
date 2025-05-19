#!/usr/bin/python3
def search_replace(my_list, search, replace):
# Create a new list where every occurence of 
    return [replace if x == search else x for x
    in my_list]