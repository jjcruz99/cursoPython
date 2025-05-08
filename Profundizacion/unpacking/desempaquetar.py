valores = [1,2,3]
print(type(valores))
print(*valores) #pude ser una lista, tupla para set **
print(*valores, sep=' - ')

def sumar(a,b,c):
    print(f'\nResultado {a+c+b}')

#Desempaquetando como argumentos directamente
sumar(*valores)

#Extraer algunos elementos de un iterable
mi_lista = [1,2,3,4,5,6]
a,b,*c = mi_lista
print(a,b,c)

a,b,c,*_ = mi_lista
print(a,b,c)

print('\n Unir listas')
lista1=[1,2,3]
lista2=[11,22,33]
lista3=[12,23,34]
lista4=[*lista1,*lista2]
print(lista4)

print('\n Unir diccionario')
dic1 = {'a':1,'b':5}
dic2 = {'c':1,'d':5}
dic3= {**dic1,**dic2}
print(dic3)

print('\n Construir una lista con una cadena')
lista_cadena = [*'Hola Mundo']
print(lista_cadena)
print(*lista_cadena,sep='')