#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===========================================
Moduli yenye darasa la Rectangle
===========================================

Darasa hili linaweza kuunda rectangle
kwa kutumia upana na urefu.
"""


class Rectangle(BaseGeometry):
    """
    Darasa la Rectangle linalorithisha kutoka kwa BaseGeometry.

    Inazindua rectangle na upana na urefu.
    """

    def __init__(self, width, height):
        """
        Inizializa Rectangle na upana na urefu.

        Hujumuisha:
        - width: Upana wa rectangle, lazima iwe nambari chanya.
        - height: Urefu wa rectangle, lazima iwe nambari chanya.

        Inatupatia:
        - Thibitisha kuwa upana na urefu ni nambari chanya
            kwa kutumia integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Kurudisha muonekano wa Rectangle kama string."""
        return f"[Rectangle] {self.__width}/{self.__height}"
