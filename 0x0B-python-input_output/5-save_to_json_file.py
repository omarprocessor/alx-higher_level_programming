#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kuandika kitu kwenye faili ya JSON
===============================
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Inahifadhi kitu (muundo wa data wa Python) kwenye faili
    kwa kutumia uwakilishaji wa JSON.

    Hoja:
        my_obj: Kitu kinachohifadhiwa kwenye faili.
        filename: Jina la faili ambalo litaundwa au kuandikwa.

    Rejesho:
        Hakuna.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
