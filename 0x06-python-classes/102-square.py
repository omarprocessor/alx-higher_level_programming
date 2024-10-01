#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square with a given size.

        Args:
            size (int or float): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int or float): The size to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Return True if this square is less than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square is less than or equal to another
           square.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Return True if this square is equal to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if this square is not equal to another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if this square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square is greater than or equal to
           another square.
        """
        return self.area() >= other.area()
