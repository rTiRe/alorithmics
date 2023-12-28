"""Найти количество простых чисел в диапазоне от 0 до n"""
def eratosphene(n: int) -> int:
    a = set(range(2, n+1))
    result = []
    while a:
        p = min(a)
        result.append(p)
        a -= set(range(p, n+1, p))
    return len(result)