#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    c = my_list[::-1]
    for i in c:
        print("{:d}".format(i))
