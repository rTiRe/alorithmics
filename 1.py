"""
Даны два числа a и b в десятичной системе счисления и основание некоторой системы счисления c.
Найдите сумму этих чисел в системе счисления c. Результат представить в виде списка.
"""

def find_sum(a: int, b: int, base: int) -> list:
    digits = '0123456789abcdefghijklmopqrstuvwxyz'
    sum_ = a+b
    c = []
    while sum_:
        c.append(digits[sum_ % base])
        sum_ = sum_ // base
    return list(reversed(c))