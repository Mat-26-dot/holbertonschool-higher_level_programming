#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end=" ")
            count += 1
        except: (IndexError, ValueError)
        break
    print()
    return count

nb_print = safe_print_list_integers([1, "a", 2], 1)
print("nb_print:", nb_print)