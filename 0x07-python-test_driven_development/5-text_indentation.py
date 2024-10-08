#!/usr/bin/python3
"""Module to indent text
"""


def text_indentation(text):
    """Prints text with 2 new lines after certain characters.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = ""
    for char in text:
        formatted_text += char
        if char in {'.', '?', ':'}:
            formatted_text += "\n\n"

    print(formatted_text.strip())
