from Profundizacion.listas.matrices import matriz

numeros = range(10)
lista_pares = []

for numero in numeros:
    if(numero%2 == 0):
        lista_pares.append(numero*numero)

print(lista_pares)

#con list comprehensions
lista_pares = [numero*numero for numero in numeros if numero%2==0]
print(lista_pares)

#otro ejm

pares = [numero for numero in range(50) if numero%2==0 if numero%6==0]
print(pares)


#otro ejemplo
impares=[]
pares =[]
[pares.append(numero) if numero%2==0 else impares.append(numero) for numero in range(20)]
print(impares)
print(pares)


print('Con una matriz ')
matriz = [[1,2,3,5],[5,6,8],[89,58,12]]
lista_simple = [valor
                for sublista in matriz
                for valor in sublista]
print(lista_simple)

print('\n Extraer los numero pares de una matriz')
pares_matriz = [valor for sublista in matriz for valor in sublista if valor%2==0]
print(pares_matriz)
