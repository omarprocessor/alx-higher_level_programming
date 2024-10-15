#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read. Default is
            an empty string.
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end="")
