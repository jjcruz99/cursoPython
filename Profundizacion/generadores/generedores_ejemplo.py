
def generador_numeros():
    for numero in range(1,6,1):
        yield numero
        print('Se reanuda la ejecucion de la funcion')

generador = generador_numeros()
print(generador)
print(type(generador))

##consumir el generador

for valor in generador:
    print(valor)

#consumir a demanda
try:
    generador = generador_numeros()
    print('consumir a demanda',next(generador))
    print('consumir a demanda',next(generador))
    print('consumir a demanda',next(generador))
    print('consumir a demanda',next(generador))
    print('consumir a demanda',next(generador))
    print('consumir a demanda',next(generador))
except Exception as e:
    print(f'\n \U00002620 Error al consumir el generador \U00002620  {e}')

    