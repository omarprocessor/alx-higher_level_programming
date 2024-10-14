#!/usr/bin/python3
"""
=============================================
Darasa la MyList linalorithisha kutoka kwenye orodha
=============================================

Darasa hili linaweza kuunda orodha na lina njia
moja ya umma iitwayo `print_sorted()` ambayo inachapisha
orodha ikiwa imepangwa kwa mpangilio wa kuongezeka.
"""


class MyList(list):
    """
    Darasa MyList linalorithisha kutoka kwenye orodha.
    """

    def print_sorted(self):
        """
        Inachapisha orodha ikiwa imepangwa kwa mpangilio wa kuongezeka.

        Hii inafanya kazi kwa kuunda nakala ya orodha, kuipanga,
        kisha kuchapisha nakala hiyo.
        """
        print(sorted(self))
