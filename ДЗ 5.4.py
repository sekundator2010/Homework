with open('t.txt', encoding='utf-8') as a:
    b = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    c = []
    for key_s in b.keys():
        d = a.readline()
        d = d.replace(key_s, b[key_s])
        c.append(d)
with open('t2.txt', 'w', encoding='utf-8') as z:
    print(''.join(c), file=z)



