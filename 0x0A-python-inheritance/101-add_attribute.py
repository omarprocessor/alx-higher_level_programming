#!/usr/bin/python3
"""
=========================
Function to add attribute
=========================

This function attempts to add an attribute to an object.
It raises a TypeError if the attribute cannot be added.
"""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
