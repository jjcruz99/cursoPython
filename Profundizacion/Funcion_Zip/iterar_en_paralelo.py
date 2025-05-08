
numeros = [1,2,3]
letras = ['a','n','b']
identificadores = 0,1,2
conjunto = {100,101,102,105}

nueva_lista = []
for numero,letra,identificador,conjunto in zip(numeros,letras,identificadores,conjunto):
    print(f'{numero} {letra} {identificador} {conjunto}')
    nueva_lista.append(f'{numero} {letra} {identificador} {conjunto}')

print(nueva_lista)

print('\nunzip')
mezcla = [(1,'x'),(2,'o'),(4,'ñ')]
lnumeros , lletras = zip(*mezcla)
print(f'Numeros: {lnumeros}  , letras : {lletras}')

print('\nOrdenar uzando zip')
mezcla = zip(lletras,lnumeros)
print(tuple(mezcla))

#Ordenar por letra
print(sorted(zip(lletras,lnumeros)))
print(sorted(zip(lnumeros,lletras)))

print('\nCrear un diccionario con un zip')

llaves = ['Nombre','Apellido']
valores = ['Juana','Perez']
diccionario1 = dict(zip(llaves,valores))

#Actualizar un elemento del dicc
llave = ['Nombre']
nuevo_nombre = 'Shailo'
diccionario1.update(zip(llave,nuevo_nombre))
print(diccionario1)
