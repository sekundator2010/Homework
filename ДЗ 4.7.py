def fibo_gen():
    for el in count(1):
        yield factorial(el)
x = 1
for i in fibo_gen():
    print('Factorial {} - {}'.format(x, i))
    if x == 15:
        break
    x += 1