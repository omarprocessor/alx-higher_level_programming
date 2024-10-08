"""
Module 0-add_integer
This module provides a function that adds two integers or floats.

"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handling infinities and NaN for floats
    if a == float('inf') or b == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if a != a or b != b:  # Check for NaN
        raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
