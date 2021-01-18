a = [6, 'Aaaa', [56, 'uuu'], (56, 'uuuu'), {2,3,4,5,6,3,1}, {'surname': 'uvarov', 'age': '180'} ]
i = 0
for i in range(len(a)):
    type_meaning = type(a[i - 1])
    print(f'{i-1}-й элемент списка имеет тип:{type_meaning}')