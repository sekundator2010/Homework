import sys

production, rate_h, premium,   = sys.argv[1:]
print(f'Заработная плата сотрудника: {int(production) * int(rate_h) + int(premium)}')