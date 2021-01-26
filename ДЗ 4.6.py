from itertools import count, cycle
#
# for i in count(int(input('Введите начальное число: '))):
#     print(i)


# b
new_list = [5, 4, 23, 10]
for i in cycle(new_list):
    if i == 10:
        break
    print(i)

# my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]

# iter = cycle(my_list)
# stop = ''
# while stop != 'q' :
#     print(next(iter), end = '')
#     stop = input()


