import modulo_funcion_sumar # importar todo el modulo
from modulo_funcion_sumar import sumar ## importar la funcion es el mas recomendado

#llamar la funcion suma
resultado = modulo_funcion_sumar.sumar(255,25656)
print(f'Resultado de la suma {resultado}')

resultado = sumar(12.3,2.69)
print(f'Resultado de la suma {resultado}')

print("\n****    Argumentos por nombre")
resultado = sumar(numero2=25,numero1=1) ##no importa el orden de los argumentos
print(f'Resultado de la suma {resultado}')

#argumentos por default
def imprimir_persona (nombre='',apellido='',edad=0):
    print(f'Hola {nombre} {apellido}  {"Eres joven" if edad < 60 else "Estas que te mueres"}')

imprimir_persona(nombre='John',edad=32,apellido='Cruz')
imprimir_persona(nombre='Andrea') #asigana la edad de 0 por defecto