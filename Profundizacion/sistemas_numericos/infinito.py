import math
from decimal import Decimal
infinito_positivo = float('inf')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

infinito_positivo = math.inf
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

infinito_positivo = Decimal('Infinity')
infinito_negativo = Decimal('-Infinity')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')