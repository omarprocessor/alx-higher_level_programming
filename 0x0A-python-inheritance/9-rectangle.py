#!/usr/bin/python3
"""
========================================
Moduli yenye darasa la BaseGeometry
========================================

Darasa hili lina kazi ya area() ambayo
inasababisha kosa ikiwa haijatekelezwa.
"""


class BaseGeometry:
    """Darasa la BaseGeometry."""

    def area(self):
        """Kazi inayoinua Exception ikiwa haijatekelezwa."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Thibitisha kuwa thamani ni nambari chanya.

        Hujumuisha:
        - name: Jina la nambari.
        - value: Thamani ya nambari, lazima iwe nambari chanya.

        Inatupatia:
        - Kosa ikiwa thamani sio nambari au ni hasi.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        - Thibitisha kuwa upana na urefu ni nambari chanya kwa
                kutumia integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Hesabu na kurudisha eneo la rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Kurudisha muonekano wa Rectangle kama string."""
        return f"[Rectangle] {self.__width}/{self.__height}"
