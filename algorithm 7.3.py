from random import randint
array = [randint(0, 100) for one_iter in range(5)]
print(array)
smaller, more = 0, 0
for two_iter in array:
    for three_iter in array:
        if array.index(three_iter) == array.index(two_iter):
            continue
        if two_iter > three_iter:
            more += 1
        if two_iter < three_iter:
            smaller += 1
    if more == len(array) // 2 and smaller == len(array) // 2:
        print(f'Искомым числом является {two_iter}')
        break
    smaller, more = 0, 0