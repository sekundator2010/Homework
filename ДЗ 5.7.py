import json
with open('t6.txt', encoding='utf-8') as a:
    average_prof, dict_firm = [], {}
    b = a.readlines()
    for u in b:
        name_f, form, proceeds, material_los = u.split()
        profit = int(proceeds) - int(material_los)
        dict_firm[name_f] = profit
        if profit > 0:
            average_prof.append(profit)
average_prof = sum(average_prof) / len(average_prof)
out_put = [dict_firm,{'average profit': average_prof}]
with open('jason.json', 'w') as z:
    json.dump(out_put, z)

with open('jason.json') as z:
    print(json.load(z))