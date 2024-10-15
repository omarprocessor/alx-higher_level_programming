#!/usr/bin/python3
"""Moduli ya mwanafunzi
"""


class Student:
    """Darasa la mwanafunzi
    """

    def __init__(self, first_name, last_name, age):
        """Inaanzisha mwanafunzi na sifa zake.

        Args:
            first_name (str): Jina la kwanza la mwanafunzi.
            last_name (str): Jina la mwisho la mwanafunzi.
            age (int): Umri wa mwanafunzi.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Rudisha mwakilishi wa kamusi wa mwanafunzi.

        Args:
            attrs (list): Orodha ya majina ya sifa za kuchukua.

        Returns:
            dict: Kamusi yenye sifa za mwanafunzi.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
