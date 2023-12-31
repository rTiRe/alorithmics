"""
Найти k-тое по счету простое число.
Число 2 считать простым числом с номером 1
"""

def is_prime(k: int):
    j = int(k ** 0.5) + 2
    for i in range(2, j):
        if k % i == 0:
            return False
    return True

def find_k_prime(k: int) -> int:
    stack = [2]
    last = 2
    while len(stack) < k:
        last += 1
        if not is_prime(last):
            continue
        stack.append(last)
    return stack[-1]

print(find_k_prime(0))