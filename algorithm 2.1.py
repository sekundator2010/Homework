# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова
# запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
result = 0
while True:
    operation = input('Введите знак производимого действия с числами. + - * / . Для остановки работы программы введите 0')
    if operation == '0':
        print('Завершение программы')
        break
    x = int(input('Введите число. По умолчанию оно будет в выражении слева'))
    y = int(input('Введите число. По умолчанию оно будет справа'))
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print('На ноль делить нельзя.')
            continue
    else:
        'Введены некорректные данные. Повторите попытку!'
    print(f'Резульльтат операции равен {result}')
