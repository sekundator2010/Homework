with open('text2.txt', encoding='utf-8') as a:
    loser, average_sal, i = [], [], 0
    while True:
        b = list((a.readline()).split())
        if b == []:
            print(f'Имена сотрудников, получающих меньше 20000:{loser}')
            print(f'Средняя зарплата сотрудников:{(sum(average_sal)) / i}')
            break
        i += 1
        salary = float(b[1])
        average_sal.append(salary)
        if salary < 20000.00:
            loser.append(b[0])

