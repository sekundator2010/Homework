# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
from random import uniform
massi_ve = [uniform(0, 50) for calculation in range(30)]
print(massi_ve)


def merge_sort(massi_ve, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(massi_ve, start, mid)
        merge_sort(massi_ve, mid, end)
        merge_list(massi_ve, start, mid, end)


def merge_list(massi_ve, start, mid, end):
    left = massi_ve[start:mid]
    right = massi_ve[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            massi_ve[k] = left[i]
            i = i + 1
        else:
            massi_ve[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            massi_ve[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            massi_ve[k] = right[j]
            j = j + 1
            k = k + 1

merge_sort(massi_ve, 0, len(massi_ve))
print('Sorted list: ', end='')
print(massi_ve)