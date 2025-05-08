
#listas son mutables

nombres = ["juan","carlos","Pedro"]
nombre2 = "laura Maria Camila Valentina".split()

#sumar listas
print(f'Sumar listas {nombres + nombre2}')

#Extender una lista
nombres.extend(nombre2)
print(f'Extender lista : {nombres}')

numeros1= [21,36,89,45,69]
print(numeros1)
#obtener el indice de un elemento
print(f'Indice de 45 : {numeros1.index(45)}')

#invertir el orden de los elementso de una lista
numeros1.reverse()
print(f'lista invertida {numeros1}')

numeros1.sort()
print(f'Lista ordenada asendente : {numeros1}')

numeros1.sort(reverse=True)
print(f'Lista ordenada descendente : {numeros1}')

print(f'\nValor minimo {min(numeros1)}')
print(f'Valo maximo {max(numeros1)}')

#Copiar los elementos de una lista a otra lista
numeros2 = numeros1.copy()
print(f'Lista copiada : {numeros2}')

print(f'\nMismo contenido ? {numeros1 == numeros2}')
print(f'Misma  referencia en memoria ? {numeros1 is numeros2}')

#copiar con constructor
numeros2 = list(numeros1)
print(f'\nMismo contenido ? {numeros1 == numeros2}')
print(f'Misma  referencia en memoria ? {numeros1 is numeros2}')

#slicing
numeros2 = numeros1[:]
print(f'\nMismo contenido ? {numeros1 == numeros2}')
print(f'Misma  referencia en memoria ? {numeros1 is numeros2}')

print('multiplicacion de listas'.center(30,'*'))
lista_multiplicacion = 5*[[2,6]]
print(lista_multiplicacion)
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)




