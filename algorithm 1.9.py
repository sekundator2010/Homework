# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))
d = [a, b, c]
min_numb, max_numb = min(d), max(d)
d.remove(min_numb), d.remove(max_numb)
print(f'Данное число является средним {d}')

