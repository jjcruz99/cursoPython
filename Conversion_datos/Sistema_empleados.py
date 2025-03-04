#programa informacion de empleados
from random import sample

print('Programa para empleados')

nombre=input('Digite el nombre del empleado:')
edad= int(input('Edad del empleado:'))
salario = float(input('Digite su salario:'))
jefe = input('Digite (si/no) si es jefe de departamento:')

#convertir a booleano
jefe = jefe.lower().strip() == 'si'

#imprimir los datos del empleado
print(f'\nDatos del empleado \nNombre: {nombre}\nEdad: {edad}')
print(f'Salario : {salario:.2f}')
print(f'Es jefe de departamento: {jefe}')
