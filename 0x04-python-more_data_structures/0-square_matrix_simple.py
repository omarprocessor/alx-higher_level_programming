#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    ls = [list(map(lambda x: x**2, row)) for row in matrix]
    return ls
