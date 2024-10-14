#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===================================
moduli yenye darasa la Rectangle
===================================
"""


class Rectangle(BaseGeometry):
    """Darasa la Rectangle ambalo linathibitisha kutoka BaseGeometry"""

    def __init__(self, upana, urefu):
        """
        Kuanzisha Rectangle na upana na urefu.

        Arguments:
        upana -- upana wa rectangle
        urefu -- urefu wa rectangle
        """
        self.integer_validator("upana", upana)
        self.__upana = upana
        self.integer_validator("urefu", urefu)
        self.__urefu = urefu

    def __str__(self):
        """Kurudisha muundo wa string wa rectangle."""
        return "[Rectangle] {}/{}".format(self.__upana, self.__urefu)

    def area(self):
        """Kurudisha eneo la rectangle."""
        return self.__upana * self.__urefu
