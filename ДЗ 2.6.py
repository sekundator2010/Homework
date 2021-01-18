cycle = 0
n = int(input('Сколько позиций хотите заполнить?'))
name = {}
price = {}
quanity = {}
unit = {}
for i in range(n):
    cycle += 1
    product = (cycle, {'Название': 0, 'Цена': 0, 'Количество': 0, 'Ед.изм.': 0})
    user_name = input('Наименование позиции:')
    product[1]['Название'] = user_name
    name_key = 'Наименование позиции:'
    name[name_key] = []
    name[name_key].insert(cycle - 1, user_name)
    user_price = int(input('Цена позиции:'))
    product[1]['Цена'] = user_price
    price_key = 'Цена позиции'
    price[price_key] = []
    price[price_key].append(user_price)
    user_quanity = int(input('Количество позиций:'))
    product[1]['Количество'] = user_quanity
    quanity_key = 'Количество позиций'
    quanity[quanity_key] = []
    quanity[quanity_key].append(user_quanity)
    user_unit = input('Укажите единицы измерения, применяемые к указанным позициям:')
    product[1]['Ед.изм.'] = user_unit
    unit_key = 'Единицы измерения позиции:'
    unit[unit_key] = []
    unit[unit_key].append(user_unit)
    print(product)
print(name)
print(price)
print(quanity)
print(unit)



