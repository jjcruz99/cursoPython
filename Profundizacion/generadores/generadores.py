# es una funcion que retorna una secuencia de valores

def generador():
    yield 1 #producir 1
    yield 2
    yield 'hola mundo'

#Consumir generador
gen = generador()
print(next(gen))
print('Se reanuda la ejecucion ')
print(next(gen))
print('Se reanuda la ejecucion ')
print(next(gen))

print(f'\nConsumiendo con un for ')
for valor in generador():
    print(valor)

