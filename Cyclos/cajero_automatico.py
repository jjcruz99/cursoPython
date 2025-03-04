print('***** Cajero Automatico')
saldo = 10000
retiro = 0
deposito = 0
salir = False
opcion = 0

while not salir:
    print(f''' Menu :
    1.Consultar saldo
    2.Retirar
    3.Depositar
    4.Salir
    ''')
    opcion = int(input('Digite opcion (1,2,3 o 4): '))
    if opcion == 4:
        salir= True
    elif opcion == 1:
        print(f'Susaldo es : {saldo} \n')
    elif opcion == 2:
        retiro = float(input('Digite el valor a retirar: '))
        if saldo > retiro:
            saldo -= retiro
            print(f'Retiro exitoso sue nuevo saldo es {saldo:.2f}\n')
        else:
            print('Su saldo es insuficiente\n')
    elif opcion == 3:
        deposito = float(input('Digite el monto a depositar: '))
        saldo += deposito
        print(f'Su nuevo saldo es: {saldo}\n')
    else :
        print('Digite un valor correcto')
else:
    print('Fin del programa')