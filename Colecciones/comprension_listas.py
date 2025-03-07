print("         compresion de listas")

numeros = []

#crear a una lista con los numeros del 1 al 20
for i in range (1,21,1):
    numeros.append(i)
print(numeros)

cuadrado = [x**2 for x in numeros]
print(cuadrado)

pares = [x for x in numeros if x % 2 == 0]
print(pares)

nombres = ["Ana", "Carlos","John"]
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)