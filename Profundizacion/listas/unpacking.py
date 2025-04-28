#desempaquetado
valores = [1,2,3]
print(valores)
print(type(valores))

valor1 , valor2, valor3 = valores
print(valor1 , valor2, valor3)

print('\nOmitir un valor o agruparlos en una sub lista')
valor1,_ ,valor3 = valores
print(valor1 , valor3)

valor1 , valor2, *valor3 = [1,2,3,4,5,6,7,8,9]
print(valor1 , valor2, valor3)

valor1 , valor2, *valor3,valor4,valor5 = [1,2,3,4,5,6,7,8,9]
print(valor1 , valor2, valor3,valor4,valor5)

print('\n Usando una funcion ')

def regresa_datos():
    return 1,2,3 # es un tupla

valor1 , valor2, valor3 = regresa_datos()
print(type(regresa_datos()))
print(valor1 , valor2, valor3)

hora = '17:20'.partition(':')
print(type(hora))

hora, separador, minutos = '17:20'.partition(':')
print(hora, separador, minutos )
