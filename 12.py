"""
Даны два сортированных списка arr1 и arr2.
Выполнить их слияние так, чтобы полученный список так же был сортирован.
"""

def merge_sort(a: list, b: list):
    i, j, c = 0, 0, []
    while True:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
            if i == len(a):
                c.extend(b[j:])
                break
        else:
            c.append(b[j])
            j += 1
            if j == len(b):
                c.extend(a[i:])
                break
    return c


print(merge_sort([12, 23, 37, 64], [15, 38]))
    