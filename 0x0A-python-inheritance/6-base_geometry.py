#!/usr/bin/python3
"""
==================================
Moduli yenye darasa la BaseGeometry
==================================

Darasa hili lina kazi ya area() ambayo
inasababisha kosa ikiwa haijatekelezwa.
"""


class BaseGeometry:
    """Darasa la BaseGeometry."""

    def area(self):
        """Kazi inayoinua Exception ikiwa haijatekelezwa."""
        raise Exception("area() is not implemented")
