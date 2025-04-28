print('Multiplicacion de cadenas '.center(60,'*'))
resultado = '*'
for contador in range (12,1,-1):
    print(f'{resultado*contador}'.center(11,' '))

resultado = 8*('Hola',' Mundo')
print(resultado)

lista = 10*[255]
print('tamaño de la lista ', len(lista))
print(lista)
