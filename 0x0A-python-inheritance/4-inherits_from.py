#!/usr/bin/python3
"""
==============================
Moduli yenye kazi ya inherits_from
==============================

Kazi hii inarudi True ikiwa kitu ni mfano wa
darasa lililorithi kutoka darasa lililotajwa,
vinginevyo inarudi False.
"""


def inherits_from(obj, a_class):
    """
    Angalia kama obj ni mfano wa darasa lililorithi kutoka a_class.

    Args:
        obj: Kitu cha kuangalia.
        a_class: Darasa la kuangalia.

    Returns:
        True ikiwa obj ni mfano wa darasa lolote lililorithi
        kutoka a_class (mojawapo ya darasa la a_class),
        vinginevyo False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
