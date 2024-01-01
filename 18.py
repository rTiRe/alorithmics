import pprint

"""
Дано N золотых слитков массой m_1, …, m_N.
Ими наполняют рюкзак, который выдерживает вес не более M.
Можно ли набрать вес в точности M?
(Задача о рюкзаке)
"""
def backpack(weights: list, m: int):
    n = len(weights)
    v = [[False] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        v[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            v[i][j] = v[i - 1][j]
            if j >= weights[i - 1]:
                v[i][j] = max(v[i][j], v[i - 1][j - weights[i - 1]])
    return v[n][m]



# print(backpack([1, 1, 1, 4, 5, 6, 7, 8], 4))