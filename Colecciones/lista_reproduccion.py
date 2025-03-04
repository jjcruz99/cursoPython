print('\n     Playlist de canciones')

#creamos la lista
lista_reproduccion = []

#agregar canciones
lista_reproduccion.append('Los caminos de la vida')
lista_reproduccion.append('El condor herido')
lista_reproduccion.append('It is my life')

#ordenar lista
lista_reproduccion.sort()

#imprimir lista
print(f'\n lis de reproduccion en orden alfabetico')
print(lista_reproduccion)
print('\nIterar lista de reproduccion')
for i in lista_reproduccion:
    print(f'-{i}')


#ordenar lista Z-a
lista_reproduccion.sort(reverse=True)
print(f'\n lista de reproduccion en ordenar de manera descendente')
print(lista_reproduccion)