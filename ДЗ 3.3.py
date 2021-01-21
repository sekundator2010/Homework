def my_func(x, y, z):
    return x,y,z
a = list(my_func(7,2,99))
numb_summ = 2
great_numb = []
for i in range(numb_summ):
    maximum_numb = max(a)
    indexation = a.index(maximum_numb)
    content = a.pop(indexation)
    great_numb.append(content)
sum = 0
for i in great_numb:
    sum += i
print(sum)