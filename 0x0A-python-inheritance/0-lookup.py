#!/usr/bin/python3
"""
=============================
Moduli yenye mbinu ya lookup
=============================
"""


def lookup(obj):
    """
    Inarejesha orodha ya sifa na mbinu zinazopatikana za kitu.

    Hoja:
        obj: Kitu ambacho sifa na mbinu zake zitatolewa.

    Rejesho:
        Orodha ya maneno ya kamba inayowakilisha majina ya sifa na
        mbinu zinazopatikana.
    """
    return dir(obj)
