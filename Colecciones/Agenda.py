
agenda = {
    'contacto1':{
      'nombre': 'john' ,
      'telefono': 2125521,
      'correo': 'john@email'
    } ,
    'contacto2':{
      'nombre': 'camila' ,
      'telefono': 60125486,
      'correo': 'camila@email'
    } ,
    'contacto3':{
      'nombre': 'jose' ,
      'telefono': 475982,
      'correo': 'john@email'
    }
}

print(agenda)
print(agenda.get('contacto1'))
print(agenda.get('contacto1').get('correo'))
print(agenda['contacto3']['nombre'])

#agregar
agenda['contacto4'] = {
    'nombre': 'Ana',
    'telefono': 120025,
    'correo': 'ana@email'
}
print(f'\n {agenda}')

##iterar diccionario
for contacto in agenda:
    print(contacto)

for contacto,detalles in agenda.items():
    print(contacto)
    print(f'''
    {detalles.get('nombre')}
    {detalles.get('telefono')}
    ''')