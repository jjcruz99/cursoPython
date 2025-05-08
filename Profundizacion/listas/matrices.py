
matriz = [[10,25],
          [36,25,50],
          [21,22,23]]
print(f'Matriz original {matriz}')
print(f'Segunda fila 3 elemento : {matriz[1][2]}')

fila = 2
columna = 2
print(f'Obtener un elemento, Fila : {fila},Columna : {columna} .Elemnto = {matriz[fila][columna]}')

matriz[0][0] = 100
print(f'Matriz modificada {matriz}')

print('\n')
print('Ordenar una matriz'.center(50,'*'))
lista_listas = [[10,12,56,25],[56,98,56],[45,69,33,699,258,22,36,97,25]]

lista_listas.sort(key=len)
print(f'Ordenar matriz por cantidad de elementos {lista_listas}')

# funciones sorted built-in
#ordenar una lista de cadenas alfabeticamente
nombres1 = ['Juan Carlos','Pedro','Anna','Luz']
nombres1 = sorted(nombres1)
print(nombres1)

nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

#ordenar por el largo de los elementos
nombres1 = sorted(nombres1, key=len)
print("ordenar por el largo de los elementos" ,nombres1)

#Retorna una lista 
nombres1 = reversed(nombres1)
print(list(nombres1))