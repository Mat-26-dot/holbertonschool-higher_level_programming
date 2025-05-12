#!/usr/bin/python3
def element_at(my_list, idx):

    if idx <0: #if idx is negative return None
        return None

    if idx >= len(my_list): #if idx is the length of my_list return None
        return None
 
    return my_list[idx] #if idx is valid return the element
