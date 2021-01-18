# numb_month = int(input('Введите натуральное число от 1 до 12'))
# month_lis = ['зима', 'зима', 'весна', 'весна', "весна", "лето", "лето", 'лето', 'осень', 'осень', 'осень', 'зима']
# if numb_month > 0 and numb_month < 13:
#     user_month = month_lis[numb_month - 1]
#     print(user_month)


try:
    numb_month = int(input('Введите натуральное число от 1 до 12'))
    print(numb_month)
except ValueError:
    print('Введены неверные значения')
except NameError:
    print('Неверно введено!')
lis_month = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето',
             8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
if numb_month > 0 and numb_month < 13:
    print(lis_month[numb_month])


