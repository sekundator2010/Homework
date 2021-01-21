def number(x, y):
    return x / y
user_x = int(input('Введите первое число'))
user_y = int(input("Введите второе число"))
try:
    decision = number(user_x, user_y)
except ZeroDivisionError:
    print('На ноль делить нельзя')
print(round(decision, 2))
