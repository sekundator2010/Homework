with open('t4.txt', 'w+', encoding='utf-8') as a:
    b = input('Введите числа')
    a.write(b)
    a.seek(0)
    c = (a.readline()).split()
    o = 0
    for i in c:
        o = o + int(i)
    print(f'Сумма записанных чисел:{(o)}')