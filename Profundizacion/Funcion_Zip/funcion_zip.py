
print(dir(__builtins__))
#help(zip)

numeros = [1,2,3]
letras = ['a','n','b']
identificadores = 0,1,2
mezcla = zip(numeros,letras,identificadores)
print(mezcla)
print(list(mezcla))
print(tuple(zip(numeros,letras)))

print(type(mezcla))


identificadores = 0,1,2,4 #
mezcla = zip(numeros,letras,identificadores)
print(list(mezcla)) # imprime la longitud de la collecion mas corta


conjunto = {100,101,102,105} #toma los elementos de forma aleatoris
mezcla = zip(numeros,letras,identificadores,conjunto)
print(list(mezcla))