#LOS SET O CONJUNTOS SON COLECCIONES DE DATOS NO ORDENADOS DE ELEMENTOS UNICOS
#NO PERMITEN ELEMENTOS DUPLICADOS

set_a = {1,2,3,4,5,6}
set_b = {'Hola',2,4,433,45,34.3,True,}
numeros = {2,2,2,1,34,45}

print(numeros)##descarta los elementos duplicados y el orden puede variar

#AGREGAR
set_b.add(78)
set_b.add('Shailo')
print(f'\n.add = {set_b}')

#ELIMINAR
set_b.remove(4)
print(f'\n.remove = {set_b}\n')

#ITERAR SET
print('\n Iterar set_b')
for elemento in set_b :
     print(elemento,end=' ')

#Comprobar si existe un elemto tambien sirve para tuplas y listas
print(f'\nComprobar si existe el elemento 4 en el set : {4 in set_b}')
print(f'\nComprobar si existe el elemento 2 en el set : {2 in numeros}')

#obtener largo del set
print(f'\n Longitud del set_b= {len(set_b)}')