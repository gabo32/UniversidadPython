import math
from decimal import Decimal

# definir not a number
a = float('NaN')
print(f'A: {a}')
print(f'Es nan (not a number) {math.isnan(a)}')

a = Decimal('Nan')
print(f'A: {a}')
print(f'Es nan (not a number) {math.isnan(a)}')


