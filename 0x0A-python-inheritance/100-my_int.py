#!/usr/bin/python3
"""
=====================================
Class definition for MyInt
=====================================

This class inherits from int and inverts the equality operators.
"""


class MyInt(int):
    """A rebel integer class that inverts == and != operators."""

    def __eq__(self, other):
        """Invert the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return super().__eq__(other)
