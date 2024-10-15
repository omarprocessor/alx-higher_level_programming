#!/usr/bin/python3
"""Mwandiko wa pascal_triangle
"""


def pascal_triangle(n):
    """Rudisha orodha ya orodha za integers zinazowakilisha
    trianguli ya Pascal.

    Args:
        n (int): Idadi ya safu za trianguli ya Pascal.

    Returns:
        list: Orodha ya orodha za integers.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Anzisha safu mpya na 1
        row = [1] * (i + 1)

        # Kazi ya kujaza safu kwa kutumia thamani za awali
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
