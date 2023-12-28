"""
Даны два числа a и b. Найдите пару чисел x и y, являющуюся решением уравнения вида:
ax + by = НОД(a, b)
РАСШИРЕНЫЙ АЛГОРИТМ ЕВКЛИДА
"""

def extended_euclidus(a: int, b: int) -> tuple:
    if b == 0:
        return a, 1, 0
    else:
        nod, x1, y1 = extended_euclidus(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
    return (nod, x, y)