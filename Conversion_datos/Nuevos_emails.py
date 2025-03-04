nombre=input('Ingrese su nombre: ')
apellido=input('Ingrese sus apellidos: ')
empresa= input('Ingrese el nombre de su empresa: ')
dominio = input('Ingrese su dominio: ')

nombre= nombre.replace(' ','.').lower().strip()
apellido= apellido.replace(' ','.').lower().strip()
empresa= empresa.strip().replace(' ','.').lower()
dominio=dominio.strip()

email= f'{nombre}.{apellido}@{empresa}.{dominio}'
print(f'\nNuevo Email es: {email}')
