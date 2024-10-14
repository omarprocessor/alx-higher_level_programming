#!/usr/bin/python3
"""
==================================
Moduli yenye darasa la BaseGeometry
==================================

Darasa hili lina kazi ya area() ambayo
inasababisha kosa ikiwa haijatekelezwa,
na integer_validator() ambayo inathibitisha
kuhusu thamani ya nambari.
"""


class BaseGeometry:
    """Darasa la BaseGeometry."""

    def area(self):
        """Kazi inayoinua Exception ikiwa haijatekelezwa."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Kazi inayothibitisha thamani ya nambari.

        Arguments:
        name -- jina la thamani
        value -- thamani ya kuthibitisha

        Hii itafanya yafuatyo:
        - Ikiwa value si nambari, inainua TypeError.
        - Ikiwa value ni ≤ 0, inainua ValueError.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
