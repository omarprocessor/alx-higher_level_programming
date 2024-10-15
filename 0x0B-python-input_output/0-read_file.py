#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kusoma faili
===============================
"""


def read_file(filename=""):
    """
    Inasoma faili ya maandishi ya UTF-8 na kuchapisha yaliyomo kwenye stdout.

    Hoja:
        filename: Jina la faili inayosomwa. Chaguo-msingi ni kamba tupu.

    Rejesho:
        Hakuna rejesho, lakini yaliyomo kwenye faili yatapakiwa kwenye stdout.
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end="")
