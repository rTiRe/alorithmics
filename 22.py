"""
Дана строка S состоящая из открывающихся и закрывающихся скобок '(' и ')'.
Найти длину наибольшей правильной последовательности скобок.
    Последовательность скобок верна если:
    * Для каждой открытой скобки есть закрытая
    * Открытые скобки должны закрываться в соответствующем порядке.
"""
def brackets(s: str):
    stack = []
    max_length = 0
    start = -1  # Индекс начала текущей правильной последовательности

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
            if start == -1:
                start = i
        else:
            if not stack:
                start = -1
            else:
                stack.pop()
                if not stack:
                    max_length = max(max_length, i - start + 1)
                else:
                    max_length = max(max_length, i - stack[-1])

    return max_length

print(brackets('((())()))'))