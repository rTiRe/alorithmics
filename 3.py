"""Реализуйте алгоритм быстрого возведения числа a в степень b."""

def power(value: int, pow: int) -> int:
    result = 1
    while pow:
        if not pow % 2:
            pow /= 2
            value *= value
        else:
            pow -= 1
            result *= value
    return result