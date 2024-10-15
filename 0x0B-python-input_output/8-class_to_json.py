#!/usr/bin/python3
"""Moduli ya darasa yangu
"""


class MyClass:
    """Darasa langu
    """

    def __init__(self, jina):
        self.jina = jina
        self.nambari = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.jina, self.nambari)


def class_to_json(obj):
    """Rudisha maelezo ya kamusi yenye muundo rahisi
    (orodha, kamusi, mfuatano, nambari na boolean) kwa ajili ya
    uakibishaji wa JSON wa kitu.

    Args:
        obj: Kigezo cha darasa.

    Returns:
        Mwakilishi wa kamusi wa sifa za kitu.
    """
    sifa = {}
    for kiwambo, thamani in obj.__dict__.items():
        if isinstance(thamani, (list, dict, str, int, bool)):
            sifa[kiwambo] = thamani

    return sifa


if __name__ == "__main__":
    m = MyClass("John")
    m.nambari = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
