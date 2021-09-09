# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
divisible_two, divisible_three, divisible_four, divisible_five = 0, 0, 0, 0
divisible_six, divisible_seven, divisible_eight,divisible_nine = 0, 0, 0, 0
for i in range(2, 100):
    if i % 2 == 0:
        divisible_two += 1
    if i % 3 == 0:
        divisible_three += 1
    if i % 4 == 0:
        divisible_four += 1
    if i % 5 == 0:
        divisible_five += 1
    if i % 6 == 0:
        divisible_six += 1
    if i % 7 == 0:
        divisible_seven += 1
    if i % 8 == 0:
        divisible_eight += 1
    if i % 9 == 0:
        divisible_nine += 1
print(f'На два без остатка делится {divisible_two}, на три {divisible_three}. на четыре {divisible_four}, на пять '
      f'{divisible_five}, на шесть {divisible_six}, на семь {divisible_seven}, на восемь {divisible_eight}, '
      f'на девять {divisible_nine}')

# Категорически не нравиться мне такое решение. Но как ещё сохранить количество раз каждого делителя?