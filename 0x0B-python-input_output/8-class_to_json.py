#!/usr/bin/python3
"""Function to convert class instance to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object's attributes.
    """
    # Create a dictionary to hold the object's attributes
    attributes = {}

    # Iterate through the object's __dict__ to get all attributes
    for key, value in obj.__dict__.items():
        # Check if the value is of a simple data structure type
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[key] = value

    return attributes
