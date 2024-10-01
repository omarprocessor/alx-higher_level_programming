#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square with a given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a
            tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position values are
            not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character # at its position.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for y in range(self.__position[1]):
            print("")  # Print the vertical spaces for position
        for x in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        String representation of the square.

        Returns:
            str: The string representation of the square.
        """
        result = []
        if self.__size == 0:
            return ""
        for y in range(self.__position[1]):
            result.append("")  # Append vertical spaces for position
        for x in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
