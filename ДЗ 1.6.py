result_day = int(input('Введите число километров, преодоленных в первый день:'))
result_all = int(input('Введите общий результат спортсмена в километрах:'))
percent = 1.1
number_cycle = 0

while result_day < result_all:
    number_cycle += 1
    if number_cycle > 1:
        result_day = result_day * percent
    print(f'{number_cycle}день: {result_day:.2f}')


