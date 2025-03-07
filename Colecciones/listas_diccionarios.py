
alumnos = [
    {
      'id':1,
      'nombre': 'John'
    },
    {
      'id':2,
      'nombre': 'Camila'
    },
    {
      'id':3,
      'nombre': 'Ana'
    }
]

#accerder
print(alumnos[0].get('nombre'))

#iterar lista de diccionarios
for contador,alumno in enumerate(alumnos): #metodo enumerate cuenta los elementos de la iteracion
    print(f'{contador} ) alumno : {alumno}')