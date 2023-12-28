"""
Дан сортированный список целых чисел arr и число x.
Найти индекс, на котором будет расположено число x в списке,
после его добавления в список в порядке сортировки.
"""

def binary_search_insert_index(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low