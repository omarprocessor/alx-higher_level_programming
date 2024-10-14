#!/usr/bin/python3
"""
=====================================
Moduli yenye darasa la Rectangle
=====================================

Darasa hili linaongeza BaseGeometry
na lina kazi ya __init__, __str__ na
kazi ya area() iliyotengenezwa.
"""


class BaseGeometry:
    """Darasa la BaseGeometry."""

    def area(self):
        """Kazi inayoinua Exception ikiwa haijatekelezwa."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Thibitisha kuwa value ni nambari chanya."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Darasa la Rectangle kinachorithishwa kutoka BaseGeometry."""

    def __init__(self, width, height):
        """Kujenga Rectangle na width na height.

        Thibitisha kuwa width na height ni nambari chanya.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Hesabu na kurudi eneo la rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Kurudi muktadha wa rectangle kama [Rectangle] <width>/<height>."""
        return f"[Rectangle] {self.__width}/{self.__height}"
