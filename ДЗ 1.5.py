proceeds_company = int(input('Введите выручки вашей фирмы:'))
costs_company = int(input('Введите сумму издержек вашей фирмы'))
profit = proceeds_company - costs_company
if profit > 0:
    print(f'Ваша выручка составляет: {profit}')
    profitability = profit / proceeds_company
else:
    print(f'Ваш убыток составляет:{profit}')

num_employee = int(input('Укажите число ваших сотрудников'))

profit_employee = profit / num_employee