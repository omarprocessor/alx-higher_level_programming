#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initialize a new Square with a given size.
        The size is stored as a private instance attribute.

        Args:
            size: The size of the square.
        """
        self.__size = size
