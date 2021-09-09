# 4. Определить, какое число в массиве встречается чаще всего.
from random import random
i, auxilary = 0, []
a = [int(random() * 100) for y in range(20)]
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


