# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint
a = [randint(-100, 100) for i in range(30)]
b = list(filter(lambda x: x < 0, a))
c = max(b)
print(f'Максимальным среди отрицательных чисел является {c}, а его положение {a.index(c)}')