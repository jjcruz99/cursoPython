
nombre = 'Sahialo'
edad = 6
sueldo = 3000000.3200
'''
%s String
%d valores enteros
%f o %.2f valores float
'''
mensaje_con_formato = 'Mi nombre es : %s'%nombre
print(mensaje_con_formato)

mensaje_con_formato = 'Mi nombre es : %s y tengo %d años '%(nombre,edad)
print(mensaje_con_formato)

persona = ('Karla','Corzo',5000000.31239)
mensaje_con_formato = 'Hola %s %s tu sueldo es  %.2f'%persona
print(mensaje_con_formato)

print('\nOtra opcion')
mensaje_con_formato = 'Hola %s %s tu sueldo es  %.2f'
print(mensaje_con_formato%persona)

print('\nOtra opcion placeholder')
mensaje_con_formato = 'Nombre {} Edad {} sueldo {:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Nombre {0} Edad {1} sueldo {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)

#cambiar el orden
mensaje_con_formato = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre,edad,sueldo)
print(mensaje_con_formato)

#argumentos por nombre
mensaje = 'Nombre {n} edad {e} sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
print(mensaje)

print('\nUsando un diccionario')
diccionario = {'nombre':'Jerjes','edad':1}
mensaje = 'Nombre {dicc[nombre]} Edad {dicc[edad]}'.format(dicc=diccionario)
print(mensaje)

print('\n F-strin Template literal '.center(50,'*'))
mensaje = f'{nombre} {edad} {sueldo:.3f}'
print(mensaje)

print('sep= ')
print(nombre,edad,sueldo, sep=', ')
