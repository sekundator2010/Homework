my_list = [44, 22, 44, 67, 12, 22, 89]
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)