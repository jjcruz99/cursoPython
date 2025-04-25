from os.path import split

#help para leer la documentacion de un modulo
#help(str.capitalize)
#help(str)
from mi_clase import Mi_clase
#help(Mi_clase)
print(Mi_clase.__doc__)
print(Mi_clase.__init__.__doc__)
print(Mi_clase.mi_metodo.__doc__)
print(Mi_clase.mi_metodo)
print(type(Mi_clase.mi_metodo))


concatenar = 'hola ' 'mundo '
concatenar += 'mas texto ' '. '
print(concatenar)

mensaje = 'hola '
mensaje2 = mensaje.capitalize()
print(f'mensaje :{mensaje}, id:{hex(id(mensaje))}')
print(f'mensaje2 :{mensaje2}, id:{hex(id(mensaje2))}')
#cualquier modificacion que se haga a un obj string crea otra posicion de memoria
mensaje2 += ' . '
print(f'mensaje2 :{mensaje2}, id:{hex(id(mensaje2))}')

print( ' Concatenar strings de una coleccion '.center(60,'*'))

tupla_str = ('Hola','Mundo','universidad','python')
mensaje = ' '.join(tupla_str)
print(mensaje)

lista_cursos = ['java','python','Spring']
mensaje = ','.join(lista_cursos)
print(mensaje)

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)

diccionario = {'nombre':'john','apellido':'cruz'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(llaves)
print(valores)

print(' Split '.center(30,'*'))
curosos = 'java python Spring' #identifica el espacio para separar los elementos
lista_cursos = curosos.split()
print(lista_cursos)

curosos = 'java,python,Spring,css,html'
lista_cursos= curosos.split(',') #idetinfica la , como elemento para separar
print(lista_cursos)

print('\nSepara solo los elementos segun la cantidad espescificada')
lista_cursos = curosos.split(',',2)#en este caso 0,1,2+3+4
print(lista_cursos)