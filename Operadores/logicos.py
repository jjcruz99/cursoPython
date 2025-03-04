#import random
print('-----------Operadores logicos----------\n')

valor1,valor2=True,False

print(f'{valor1} and {valor2} = {valor1 and valor2}')
print(f'{valor1} or {valor2} = {valor1 or valor2}')
print(f'{valor1} Not = {not valor1}')

nombre = 'Hola'
comprobar_cadena_vacia= not nombre
print(f'Comprobar si una cadena esta vacia : {comprobar_cadena_vacia}')

nombre = None
comprobar_cadena_vacia= not nombre
print(f'Comprobar si una cadena esta vacia : {comprobar_cadena_vacia}')