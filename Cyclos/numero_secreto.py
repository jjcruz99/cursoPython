print('\n***************Numero secreto**********\n')
import random
contador = 0
numero_secreto= random.randint(1,50) ### GENERA UN NUMERO ALEATORIO
numero_comparador = 0
intentos = 0
##print(numero_secreto)
while contador < 5 :
    numero_comparador = int(input('Digite un numero entre (1-50): '))
    intentos += 1
    contador += 1
    if numero_secreto == numero_comparador:
        contador = 12
        print(f'Adivinaste felicitaciones {numero_secreto}\n')
    elif numero_secreto > numero_comparador:
         print('El numero secreto es mayor, vuelve a intentar\n')
    else:
        print('El numero secreto es menor, vuelve a intentar\n')

else:
    print(f'Fin del juego intentos realizados {intentos}')