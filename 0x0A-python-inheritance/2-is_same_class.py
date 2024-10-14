#!/usr/bin/python3
"""
==============================
Moduli yenye kazi ya is_same_class
==============================

Kazi hii inarudi True ikiwa kitu ni mfano sahihi
wa darasa lililotajwa; vinginevyo inarudi False.
"""


def is_same_class(obj, a_class):
    """
    Angalia kama obj ni mfano wa a_class.

    Args:
        obj: Kitu cha kuangalia.
        a_class: Darasa la kuangalia.

    Returns:
        True ikiwa obj ni mfano sahihi wa a_class, vinginevyo False.
    """
    return type(obj) is a_class
