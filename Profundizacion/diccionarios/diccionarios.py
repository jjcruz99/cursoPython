from pprint import pprint as pp

dicc1 = {
    'nombre':'juan',
    'apellido':'perez',
    'edad' : 85
}
print(dicc1)

#las llaves son inmutables
dicc2 = {
    (1,2):'Valor1'
}

#Si no encuentra la llave la crea
dicc2['area'] = 'Sistemas'
print(dicc2)

dicc2['area'] = 'electronica'
print(dicc2)

print('Recuperar valores ')
print(dicc2['area'])#si no la encuentra lanza una exepcion

#metogo get
print(dicc2.get('area'))
print(dicc2.get('arrea','No se encontro la llave'))

#setdefault si modifica el diccionario si no encuentra la clave
nombre = dicc1.setdefault('nombre','Valor por default')
print(nombre)

nombre = dicc1.setdefault('nombres','Valor por default')
print(nombre)
print(dicc1)

#from pprint import pprint as pp
help(pp)
print('\n Imprimir con print \n')
pp(dicc1)

