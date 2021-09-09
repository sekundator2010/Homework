# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint
d = [randint(0, 100) for i in range(23)]
e, f, h = max(d), min(d), 0
g = [h + k for k in d[f : e] if k != e and k != f]
print(sum(g))