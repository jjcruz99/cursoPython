print('\n***********Dibujar triangulo equilatero\n**********')

numero_filas = int(input('Digite numero de filas "debe ser mayo a 2": '))
print('\n')

###mi codigo
if numero_filas >= 2:
    for i in range(numero_filas + 1):
        if i == 0:
            print('       *')
        elif i== 1:
            print('      ***')
        elif i== 3:
            print('     *****')
        elif i == 4:
            print('    *******')
        elif i == 5:
            print('   *********')
else:
    print(f'Numero de filas insufeciente para dibujar un triangulo')

print('\n Codigo clase\n')
for fila in range(1,numero_filas + 1):
    espacios_blanco= ' ' * (numero_filas - fila) #Multiplicacion de cadenas
    asteristicos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteristicos}')

