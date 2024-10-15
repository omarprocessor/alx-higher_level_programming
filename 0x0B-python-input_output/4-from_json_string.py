#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kubadilisha JSON kuwa kitu
===============================
"""

import json


def from_json_string(my_str):
    """
    Inarejesha kitu (muundo wa data wa Python) kilichowakilishwa
    na kamba ya JSON.

    Hoja:
        my_str: Kamba ya JSON inayowakilisha kitu.

    Rejesho:
        Kitu kilichoweza kubadilishwa kutoka kwa kamba ya JSON.
    """
    return json.loads(my_str)
