
#Elementos unicos

#set vacio
conjunto = set()
print(type(conjunto))

conjunto.add('Juan')
conjunto.add('Juan')
print(conjunto)

# crear un set a partir de un iterable
conjunto = set([4,5,7,8,8])
print(conjunto)

print('\nAgregar elementos a un set ')
conjunto2 = {100,0,36,85,8}
conjunto2.update(conjunto)
print(conjunto2)

print('\nCopiar un set a otro')
conjunto_copia = conjunto2.copy()
print(conjunto_copia)
print(f'Es igual en contenido: {conjunto2 == conjunto_copia}')
print(f'Es la misma referencia: {conjunto2 is conjunto_copia}')
