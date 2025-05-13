#!/usr/bin/python3
def no_c(my_string):

    result = []    # Step 2: Create an empty list to hold charcters

    for char in my_string:    # Step 3: Go through each character in string

        if char != 'c' and char != 'C':    # Step 4: If char is not 'c' or 'C'

            result.append(char)    # append characters in new_string
    new_string = ''.join(result)   # Step 5: Combine the list into a new_string

    return new_string    # Step 6: Return the new_string
