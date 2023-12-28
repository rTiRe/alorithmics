"""
Даны два сортированных списка arr1 и arr2.
Выполнить их слияние так, чтобы полученный список так же был сортирован.
"""

def merge_two_list(a: list, b: list):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

# def merge_sort(arr: list):
#     l = len(arr)
#     if l == 1:
#         return arr
#     middle = l // 2
#     left = merge_sort(arr[:middle])
#     right = merge_sort(arr[middle:])
#     return merge_two_list(left, right)

# print(merge_two_list([12, 23, 37, 64], [15]))
    