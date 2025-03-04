print('**********Login***********')
password='31498Jj'
user='admin'

password_validacion= input('Por favor digite su Usuario: ')
user_validacion=input('Por favor digite su clave: ')
acceso=password_validacion == password and user_validacion == user

print(f'Datos correctos = {acceso}')

