"""
Даны два числа a и b. Найдите их наибольший общий делитель.
АЛГОРИТМ ЕВКЛИДА
"""

def NOD(a: int, b: int) -> int:
    try:
        r = a % b
    except ZeroDivisionError:
        return abs(a)
    if not r:
        return abs(b)
    return NOD(b, r)