"""
Даны две последовательности,
требуется найти длину их наибольшей общей подпоследовательности.
"""
def lcs(s1: str, s2: str):
    n = len(s1)
    m = len(s2)
    lens = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                lens[i][j] = lens[i - 1][j - 1] + 1
            else:
                lens[i][j] = max(lens[i - 1][j], lens[i][j - 1])

    return lens[n][m]


print(lcs("abcabaac", "baccbca"))  # Вывод: 4