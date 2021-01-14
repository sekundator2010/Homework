num_user = int(input('Введите число'))
num_cycles = 0
max_numb = 0
while num_user > 0:
    num_cycles += 1
    remainder_numb = num_user % 10
    num_user = num_user // 10
    if num_cycles == 1:
            max_numb = remainder_numb

    if max_numb <= remainder_numb:
            max_numb = remainder_numb
print(max_numb)

