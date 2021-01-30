with open('text1.txt', 'w+') as files:
    while True:
        data = input('Введите строку символов:')
        if data == '':
            break
        files.write(data + '\n')
