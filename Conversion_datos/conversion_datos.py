##Casting o conversion de datos
print('Entrada y conversion de datos')
numero_cadena = '109'
numero_entero = int(numero_cadena)
suma = numero_entero + numero_entero
print(f'Resultado de la suma {suma}')

texto_num='3.14156'
numero_float= float(texto_num)
print(f'Cadena a flotante : {numero_float}\n')

print('Conversion numerica a cadena')
numero_cadena = str(numero_float)
print(f'{numero_cadena}')

print('Conversion booleano')
numero_o=0
booleano = bool(numero_o)
print(f'{booleano}')

numero_o=7
booleano = bool(numero_o)
print(f'{booleano}')

numero_o=''##cadena vacia devuelve false
booleano = bool(numero_o)
print(f'{booleano}')

numero_o='BBBB'##cadena no vacia
booleano = bool(numero_o)
print(f'Cadena no vacia {booleano}')

varieble= None
booleano = bool(varieble)
print(f'varieble= None {booleano}')