#una tupla es igual a una lista coleccion de datos ordenados pero las tuplas son inmutables
# en numero de datos y los datos.
print('\n Tuplas ')
tupla_numeros = (1,2,3,4,5)
tupla_mixta = ('hola',68,'Mundo',78,'JJ')
tupla_sin_parentisis = 'john', 'Cruz'#es opcional el uso de los parentisis
tupla_un_elemento = 89,
tupla_anidada = 23,(24,25),(27,28),99 # es una tupla dentro de otra tupla

print(len(tupla_numeros))
#iterar
for i in tupla_mixta:
    print(i,end=' ')

print('\nAcceder a un indice de una tupla')
print(f'Accediendo al subindice tupla_mixta[2]= {tupla_mixta[2]}\n')


