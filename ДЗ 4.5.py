from functools import reduce
def mul_list(x, y):
    return x * y

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(mul_list, my_list))
