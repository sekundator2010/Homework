all_seconds = int(input('Введите предполагаемое число секунд!'))
remainder_seconds = all_seconds % 60
num_min_intermediate = all_seconds // 60
remainder_minutes = num_min_intermediate % 60
num_hour = num_min_intermediate // 60
print(f'В {all_seconds} всего часов: {num_hour} минут: {remainder_minutes} и секунд: {remainder_seconds} ')