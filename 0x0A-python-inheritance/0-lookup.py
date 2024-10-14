#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        A list of strings representing the names of the available
        attributes and methods.
    """
    return dir(obj)
