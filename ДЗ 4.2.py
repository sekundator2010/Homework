old_list = [21,23,45,34.6,34,233]
new_list = [num for i, num in enumerate(old_list) if num > old_list[i - 1] and i != 0]
print(new_list)