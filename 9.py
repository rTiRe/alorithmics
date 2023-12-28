"""
Дан список целых чисел arr. Реализовать сортировку простыми обменами,
в качестве результата вернуть количество перестановок выполненных в процессе сортировки.
"""
def bubble_sort(arr: list) -> int:
    l = len(arr)
    count = 0
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    return count