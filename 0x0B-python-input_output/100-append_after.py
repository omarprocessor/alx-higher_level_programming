#!/usr/bin/python3
"""Mwandiko wa append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing
             a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to insert after each line
                containing search_string.
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
