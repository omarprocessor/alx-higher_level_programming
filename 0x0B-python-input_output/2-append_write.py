#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kuongeza maandishi kwenye faili
===============================
"""


def append_write(filename="", text=""):
    """
    Inaongeza kamba mwishoni mwa faili ya maandishi ya UTF-8 na
    inarejesha idadi ya wahusika walioongezwa.

    Hoja:
        filename: Jina la faili inayosomwa au kuandikwa. Chaguo-msingi ni
        kamba tupu.
        text: Maandishi yanayoandikwa kwenye faili. Chaguo-msingi ni
        kamba tupu.

    Rejesho:
        Idadi ya wahusika walioongezwa kwenye faili.
    """
    with open(filename, 'a', encoding='UTF-8') as file:
        return file.write(text)
