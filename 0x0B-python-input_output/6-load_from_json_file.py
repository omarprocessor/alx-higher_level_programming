#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kupakia kitu kutoka faili ya JSON
===============================
"""

import json


def load_from_json_file(filename):
    """
    Inasoma faili la JSON na inaunda kitu kutoka kwa uwakilishaji wake.

    Hoja:
        filename: Jina la faili la JSON.

    Rejesho:
        Kitu kinachoundwa kutoka kwa JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
