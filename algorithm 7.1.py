# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
from random import randint

def bubble(arra_y):
    n = 1
    while n < len(arra_y):
        for i in range(len(arra_y) - n):
            if arra_y[i] > arra_y[i + 1]:
                arra_y[i], arra_y[i + 1] = arra_y[i + 1], arra_y[i]
        n += 1
    return arra_y
mass_ive = [randint(-100, 100) for calculation in range(30)]
print(mass_ive)
phial = bubble(mass_ive)
print(phial)