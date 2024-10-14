#!/usr/bin/python3
"""
==============================
Moduli yenye kazi ya is_kind_of_class
==============================

Kazi hii inarudi True ikiwa kitu ni mfano wa
darasa lililotajwa au ikiwa ni mfano wa
darasa lililorithi kutoka darasa hilo; vinginevyo inarudi False.
"""


def is_kind_of_class(obj, a_class):
    """
    Angalia kama obj ni mfano wa a_class au
    ni mfano wa darasa lolote lililorithi kutoka a_class.

    Args:
        obj: Kitu cha kuangalia.
        a_class: Darasa la kuangalia.

    Returns:
        True ikiwa obj ni mfano wa a_class au
        darasa lolote lililorithi kutoka a_class,
        vinginevyo False.
    """
    return isinstance(obj, a_class)
