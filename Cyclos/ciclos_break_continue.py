print('\n   \n     Break    ')

for numero in range (1,10):
    if numero % 2 == 0  : #numeros pares
        print(numero)
        break  ## termina la ejecucion del ciclo  en este caso cuando encuentra el primner numero par


print('\n      Continue\n')
for numero in range (1,10):
    if numero % 2 == 1: # numero impar
        continue #Continua y no realiza ninguna accion
    print(numero,end='-')