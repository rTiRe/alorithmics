"""
Дан список целых чисел arr.
Реализовать сортировку вставками (без использования бинарного поиска),
в качестве результата вернуть количество перестановок выполненных в процессе сортировки.
"""
def insertion_sort(arr: list) -> int:
    count = 0
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]
            j-=1
            count += 1
        arr[j+1] = k
    return count, arr

print(insertion_sort([12, 5, 24]))