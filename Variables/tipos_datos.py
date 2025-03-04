#entro
import math

edad=32
#float
promedio=9.87
#str
cadena= 'Hola a todos'
#booleano
es_estudiante= False

#none ausencia de valor
direccion = None

#las constantes se declarar en mayusculas
PI=3.14159
print(PI)

#usar constantes del lenguaje python
print('valor de pi: ', math.pi)

#string multiple
cadena_multiple= ''' hola
                          mundo
                              :)'''
print(cadena_multiple)

###############las cadenas estan indexadas osea cada letra tiene un numero correspondiente a la posicion como un vector.

frase = "Hola Sahilo"
print(frase)
#recuperar el primer caracter
primer_caracter= frase[0]
print("La primera letra de la cadena (",frase,") es : ", primer_caracter)
ultimo_caracter= frase[10]
print("La primera letra de la cadena (",frase,") es : ", ultimo_caracter)

############# las cadenas son inmutables al cambiar el valor se crea un nuevo objeto. no podemos cambiar uno de sus indices.

#el siguiente codigo genera un error
#intentar cambiar la primera letra a minuscula
#frase[0] = "h"
   #frase[0] = "h"
   # ~~~~~^^^
   #TypeError: 'str' object does not support item assignment

