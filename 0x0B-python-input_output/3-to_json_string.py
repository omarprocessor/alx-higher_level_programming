#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kubadilisha kitu kuwa JSON
===============================
"""

import json


def to_json_string(my_obj):
    """
    Inarejesha uwakilishi wa JSON wa kitu kilichopewa (kamba).

    Hoja:
        my_obj: Kitu ambacho kinapaswa kubadilishwa kuwa JSON.

    Rejesho:
        Uwakilishi wa kamba wa kitu katika muundo wa JSON.
    """
    return json.dumps(my_obj, ensure_ascii=False)
