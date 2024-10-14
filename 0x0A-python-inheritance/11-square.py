#!/usr/bin/python3
"""
=====================================
Class definition for Square
=====================================

This class inherits from Rectangle
and implements methods for __init__, area, and __str__.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize a square with a given size.

        Validates that size is a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
