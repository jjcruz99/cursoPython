#Los diccionarios son una coleccion ordenada desde py3.7
#se almacenan clave valor

mi_diccionario = {'clave1': "Hola",
                  'clave2' : "mundo",
                  'clave3': 2
                  }
print(f'Dicionario \n{mi_diccionario}')
print(mi_diccionario['clave3'])
print(mi_diccionario.get('clave3'))
print(mi_diccionario.keys()) #obtener todas la clave

#iterar
for llave , valor in mi_diccionario.items():
    print(f'Llave: {llave} , valor: {valor}')

for valor in mi_diccionario.values():
    print(f'Valores : {valor}')

for clave in mi_diccionario.keys():
    print(f'Claves : {clave}')

#modificar
mi_diccionario['clave3'] = 99

#agregar
mi_diccionario['calve4'] = "todos"

#eliminar
del mi_diccionario['clave1']
print(mi_diccionario)

mi_diccionario.pop('clave2')
print(mi_diccionario)


