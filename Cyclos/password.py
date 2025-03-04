print('***** Programa creacion y validacion de Password ')

validacion = False
password = ''
num_caracteres= 0
while not validacion:
    password = input('Digite una contraseña debe tener minimo 6 caracteres: ')
    for letra in password:
        num_caracteres += 1
    if num_caracteres >=6:
        print('Contraseña dentro del rango')
        validacion = True
    else:
        print('Digite una contraseña valida\n')
        num_caracteres =0
else:
    print('Fin del programa')