#  4. Определить, какое число в массиве встречается чаще всего.
# Она достаточно обьёмная, разница должна быть видна
import time
from random import random, randint
from collections import Counter
start = time.time()
i, auxilary = 0, []
a = [int(random() * 100) for y in range(500)]
for number in a:
    i += 1
    numb = a.count(number)
    auxilary.append(numb)
    if i == 1:
         maxi_mum = numb
    elif maxi_mum < numb:
        maxi_mum = numb
    elif maxi_mum > numb:
        maxi_mum = maxi_mum
print(f'Наибольшее число вхождений у элемента {a[auxilary.index(maxi_mum)]}')
print(time.time() - start)

# На cProfaile и timeit всё - таки требуются определённые вещи. Для timeit требуется заключить в скобки всё выражение а для
# cProfaile нужна функция, которая запускает всю программу ( пробовал запихать под скобки цикл, но ничего не вышло). Для
# теста не подходили программы где много ручного ввода т.к. будем считать не скорость программы, а скорость
# ввода человека что неверно. Теперь приведу образцовый пример решения HW
start_1 = time.time()
init_list = [randint(0,1) for _ in range(500)]
print(init_list)
print(Counter(init_list).most_common(1))
print(time.time() - start_1)

# Вписав в количество итераций значение 500 наглядно увидел что более короткое и лаконичное действие занимает 0,0009,
# а моё 0,0029. Разница весьма ощутима ( даже несмотря на то, что единица в Counter взята с потолка)



