# def a(x):
#     x += x
reserve = []
i = 0
def number(x):
    return x
while i != 'q' or i != 'Q':
    user_numb = input('Вводите числа. Для выхода из программы введите букву q').split()
    for i in user_numb:
        if i == 'q' or i == 'Q':
            print(f'Текущая сумма:{sum(reserve)}. Завершение работы')
            break
        reserve.append(int(i))
    d = reserve.copy()
    g = (map(number, d))
    print(f'Сумма всех чисел:{sum(g)}. Продолжаем дальше!')