#!/usr/bin/python3
"""
===============================
Moduli yenye mbinu ya kuandika faili
===============================
"""


def write_file(filename="", text=""):
    """
    Inaandika kamba kwenye faili ya maandishi ya UTF-8 na
    inarejesha idadi ya wahusika waliowekwa.

    Hoja:
        filename: Jina la faili inayosomwa au kuandikwa. Chaguo-msingi ni
        kamba tupu.
        text: Maandishi yanayoandikwa kwenye faili. Chaguo-msingi ni
        kamba tupu.

    Rejesho:
        Idadi ya wahusika waliowekwa kwenye faili.
    """
    with open(filename, 'w', encoding='UTF-8') as file:
        return file.write(text)
