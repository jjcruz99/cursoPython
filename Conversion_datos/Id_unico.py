import random

from Valores_aleatorios import numero

print('**********Programa Id Unico')
nombre=input('Digite su nombre: ')
apellido= input('Digite su apellido: ')
nacimiento = input('Digite su año de nacimiento: ')

#eliminar espacios al inicio y final
nombre=nombre.strip()
nacimiento=nacimiento.strip()

#obtener las dos letras y ponerlas en mayusculas
nombre=nombre[0:2].upper()
nacimiento=nacimiento[2:4]
numero_aleatorio= random.randint(1000,9999)

# hacer todo lo anterior en una sola linea
apellido=apellido.strip().upper()[0:2]

numero_str= str(numero_aleatorio)
id=(nombre + apellido + nacimiento + numero_str) ##''.join([cadena1,' ',cadena3,' ',cadena2])
print(f'\n Id Generado: {id}')