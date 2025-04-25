
valor = 0
resoultado = bool(valor)
print(resoultado)

valor = 15.36
resoultado = bool(valor)
print(resoultado)

valor = ''
resoultado = bool(valor)
print(resoultado)

valor = 'bbg'
resoultado = bool(valor)
print(resoultado)

#colecciones
valor = []
resoultado = bool(valor)
print(resoultado)

valor = [5.6,236]
resoultado = bool(valor)
print(resoultado)

valor = ()
resoultado = bool(valor)
print(resoultado)

valor = (5.6,236)
resoultado = bool(valor)
print( resoultado)

valor ={
    'nombre' : 'John',
    'Apellido': 'Cruz'
    }
resoultado = bool(valor)
print( resoultado)

print('Conversion explicita'.center(30,'*'))
if bool(''):
    print('verdadero')
else:
    print('falso')

if 'A':
    print('verdadero')
else:
    print('falso')