# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random
a = [[int(random() * 100) for i in range(10)], []]
maximum = a[0].index(max(a[0]))
minimum = a[0].index(min(a[0]))
a[0][maximum], a[0][minimum] = a[0][minimum], a[0][maximum]
print(a)