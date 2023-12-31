"""
Вычислите n-й член последовательности, заданной формулами:
a_2n = a_n + a_n-1
a_2n+1 = a_n - a_n-1
a_0 = a_1 = 1
"""

def find_n(n: int):
    if n == 0 or n == 1:
        return 1
    a = [0] * (n + 1)
    a[0] = a[1] = 1
    for i in range(2, n+1):
        m = i // 2
        if i % 2 == 0:
            a[i] = a[m] + a[m-1]
        else:
            a[i] = a[m] - a[m-1]
    return a[n]
