my_list = [8, 6, 5, 5, 4 , 2]
val = int(input('Введите натуральное число:'))
for i in range(len(my_list)):
    if val > my_list[i]:
        my_list.insert(i, val)
        print(my_list)
        break
    elif val == my_list[i]:
        my_list.insert(i + 1, val)
        print(my_list)
        break
    elif len(my_list) == i + 1:
        my_list.append(val)
        print(my_list)
        break



