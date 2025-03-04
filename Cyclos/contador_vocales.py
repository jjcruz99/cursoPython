print('\n Contador de vocales')

cadena = 'Hola Mundo'
contador = 0
print(cadena[0] == 'H')
print(len(cadena))
for i in range (len(cadena)):
    print(i)
    if cadena[i] == 'a' or cadena[i] == 'e' or cadena[i] == 'i' or cadena[i] == 'o' or cadena[i] == 'u':
        contador += 1

print(f'Cantidad de vocales= {contador}')
