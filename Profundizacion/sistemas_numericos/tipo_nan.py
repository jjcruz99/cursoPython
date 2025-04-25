from decimal import Decimal
import math
#NaN not a number - no es sensible a mayusculas y minusculas
a= float('NaN')
print(f'a:{a}')

print(f'Es a =  nan ? : {math.isnan(a)}')

a = Decimal('nan')
print(f'Es a =  nan ? : {math.isnan(a)}')