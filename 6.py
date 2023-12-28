"""Проверить, является ли число a простым."""

def is_prime(a: int) -> bool:
    if a == 2:
        return True
    j = int(a ** 0.5) + 1
    for i in range(2, j + 1):
        if a % i == 0:
            return False
        return True