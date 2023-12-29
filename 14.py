"""Реализовать алгоритм быстрой сортировки."""

def partition(arr: list, low: int, high: int):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr: list, low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# array = [1, 8, 6, 0, 3]
# quick_sort(array, 0, len(array) - 1)
# print(array)