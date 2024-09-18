#!/usr/bin/python3

def uniq_add(my_list=[]):
    myset = {i for i in my_list}
    total = sum(myset)
    return total
