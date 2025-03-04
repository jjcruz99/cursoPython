#from lista_reproduccion import lista_reproduccion

print('\n          Lista de reproduccion')
lis_reproduccion = []
cancion = ''

##solicitar nombre de la cancion
while not cancion == 'Salir' :
   cancion = input('Digite el nombre de la cansion o salir: ')
   cancion = cancion.lower().strip()## Eliminar espacio y poner todo en minuscula
   cancion = cancion[0].upper() + cancion[1:len(cancion)] ## poner la primera letra en minuscula
   lis_reproduccion.append(cancion) ##agregamos la cancion en la lista

#ordenar lista A-Z
lis_reproduccion.remove('Salir')
lis_reproduccion.sort()

#iterar lista
print('\nTu Lista de reproduccion\n')
for i in lis_reproduccion:
    print(f'->{i}')