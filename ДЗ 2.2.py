mega_list = []
n = 1
while True:
    user_list = input('Введите символы для заполнения списка. Для начала обмена символов в списке нажмите "достаточно"')
    if user_list != 'достаточно':
        mega_list.append(user_list)
    elif user_list == 'достаточно':
        for numb_list in range(len(mega_list) // 2):
            mega_list[n], mega_list[n - 1] = mega_list[n - 1], mega_list[n]
            n += 2
        print(mega_list)
        break



