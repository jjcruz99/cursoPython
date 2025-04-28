
contenido = 'Universidad Universidad Universidad Universidad PYTHON HOLA mundo'

#contar cuantas veces aparece la palabra Universidad
print(contenido.count('Universidad'))

print(contenido.upper())
print(contenido.lower())

#buscar la palabra python
print('python'.lower() in contenido.lower())

#comrovar si una cadena inicio o termina con
print('Inicio y final de una cadena ')
print(contenido.lower().startswith('universidad'.lower()))
print(contenido.lower().endswith('mundo'.lower()))

print('\nPreguntar si una cadena esta toda en mayuscula o miniscula Islower y isUper')
print(contenido.islower())
print(contenido.isupper(),'\n')

print(' Alinear cadenas '.center(60,'*'))

titulo = 'Clase de String'
print(titulo.center(50,'+'))

print(titulo.center(len(titulo)+10,'-'))

#justificar a la izquierda y derecha
print(titulo.ljust(len(titulo)+12,'.'))
print(titulo.rjust(len(titulo)+12,'.'))

print('Reemplazar el contenido ')
print(contenido.replace(' ','+'))

print('\nEliminar caracteres al inicio y final')
titulo = '  ***++++ ++++ ++++*** '
print(titulo.strip())
titulo = '***++++ ++++ ++++***'
print(titulo.strip('*'))

print(titulo.lstrip('*'))
print(titulo.rstrip('*'))

#aplicar varios strip()
titulo = '  *** ++++ ++++ ++++ *** '.strip().strip('*').strip()
print(titulo)











