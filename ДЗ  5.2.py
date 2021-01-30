with open('text1.txt') as a:
    i, c = 1, 0
    while True:
        b = a.readline()
        if b == '':
            print(f'Количество строк равно:{i - 1}')
            print(f'Количество символов во всех строках:{c}')
            break
        c = c + len(b)
        i += 1