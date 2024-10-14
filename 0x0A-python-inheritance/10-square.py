#!/usr/bin/python3
"""
=====================================
Moduli yenye darasa la Square
=====================================

Darasa hili linaongeza Rectangle
na lina kazi ya __init__ na area().
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Darasa la Square kinachorithishwa kutoka Rectangle."""

    def __init__(self, size):
        """Kujenga Square na size.

        Thibitisha kuwa size ni nambari chanya.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Hesabu na kurudi eneo la square."""
        return self.__size ** 2

    def __str__(self):
        """Kurudi muktadha wa square kama [Rectangle] <size>/<size>."""
        return f"[Rectangle] {self.__size}/{self.__size}"
