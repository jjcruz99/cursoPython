
multiplicacion = (valor * valor for valor in range(1,4))

print(type(multiplicacion))
for valor in multiplicacion:
    print(valor)

try:
    print(next(multiplicacion))
except StopIteration as e:
    print('\U00002620 No se pudo llamar el generador ERROR',e)


#tambien se puede pasar una expresion generadora a una funcion sin parentesis
#funciopn sum()
sumaturia = sum(valor * valor for valor in range(1,4))
print(sumaturia)


lista = ['Juan','Camila']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

print('\nCrear un strin a partir de un generador')
contador = 0

def incrementar():
    global contador
    contador +=1
    return contador

generador = (f'{incrementar()}.{nombre}' for nombre in lista)
lista = list(generador)
print(generador)
cadena = ', '.join(lista)
print(cadena)




