#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===================================
    Moduli yenye darasa la Rectangle
===================================
"""


class Rectangle(BaseGeometry):
    """
        Darasa la Rectangle linalorithisha kutoka kwa BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
