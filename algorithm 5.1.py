# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
import collections
defdict = collections.defaultdict(list)
value = int(input('Введите количество компаний, учавствующих в сравнении'))
sum_profit, summ = [], 0
for q in range(value):
    name_company = input('Введите название компании')
    profit_1 = int(input('Введите первый показатель выручки.'))
    profit_2 = int(input('Введите второй показатель выручки.'))
    profit_3 = int(input('Введите третий показатель выручки.'))
    a = profit_1 + profit_2 + profit_3
    defdict[name_company].append(a)
print(defdict)
for u in defdict.values():
    sum_profit.append(u)
    summ += u[0]
average = summ / len(defdict.values())
print(f'Средняя выручка компаний {average}')
for key, item in defdict.items():
    if item[0] > average:
        print(f'Выручка компании {key} выше среднего у выборки')
    elif item[0] < average:
        print(f'Доходы компании {key} ниже среднего у выборки')


