#Estructura IF
print('*******Sentencia IF******\n')
edad =int(input('Digite su edad: '))
if edad == 0:
    input(f'El valor digitado es erroneo \nSu edad es= {edad}')
elif edad >= 18:
    print (f'Es mayor de edad \nSu edad es= {edad}')
else:
    input(f'Es menor de edad \nSu edad es= {edad}')


###Logica inversa
print('\n Logica inversa \n')
salir = input('Digite "Si/No" si desea salir del programa: ')
salir = salir.strip().lower() == 'si'   #la varieble se vuelve booleana
print(salir)
if not salir:
    print('Continua en el programa')
else:
    print('Salio del programa')
