#son colecciones ordenadas  y mutablesde leementos que pueden ser de diferentes tipos de datos.
from iterar_listas import lista_mixta

print('\n        Ejemplos de listas \n')

numeros = [1,211,1,1.25555810285,89]
frutas = ['banano','Manazana','Pera','fresa']
mixta = [1,'Perro',2.369,'Carro',[4,25.6],'Hola']#inculoso una lista dentro de una lista

print(f'\nLargo de una lista: {len(numeros)}')

print(f'\nAccdeder a un indice de una lista, frutas[3]: {frutas[3]}')
print(f'\nAccdeder a un indice de una lista, frutas[-1]: {frutas[-1]}')# con numeros negativos el -1 es el ultimo indice de la lista

print('\nModificar el valor de un indice')
numeros[0]= 3.14156
print(f'Nuevo dato del indice[0]= {numeros[0]}')

####################################
print('\nAgregar nuevos elementos a una lista')
print(f'Lista inicaial: {frutas}')
frutas.append('Guanabana')
print(f'\nLista con un nuevo dato al final metodo apped: {frutas}')
frutas.insert(2,'Guayaba')#inserta en el indice 2 el nuevo valor y desplaza los demas elementos hacia la derecha
print(f'\nLista con un nuevo dato metodo insert: {frutas}')

###########
print('\nEliminar un elemento de la lista ')
frutas.remove('banano')
frutas.pop(1)##elimina el indice 1
del numeros[2]##elimina el indice 1
print(frutas,end=' ')

#########sub lista
print('\nSub lista')
sublista = numeros[1:3] # Gernera una sub lista del indice 1 al 2 (Sin incluir el 3)
print(f'\nSub lista = {sublista}')

###sumar toda una lista
sumatoria = sum(numeros)
print(f'\nSuma de todos los valores de una lista funcion sum() : {sumatoria}')

print(f'\nRecorer una lista co un ciclo for')
for i in frutas:
    print(i)

#Comprobar si existe un elemto tambien sirve para tuplas y listas
print(f'\nComprobar si existe el elemento 2.369 en el set : {2.369 in lista_mixta}')