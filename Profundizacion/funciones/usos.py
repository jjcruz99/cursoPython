
#frist class citizens
def sumar(a,b):
    return a+b

#asiganar funcion a una variable
mi_funcion = sumar

resultado = mi_funcion(9,6)
print(resultado)

# 2.funcion como argumento
def operacion(a,b,sumar_arg):
    print(f'Resultado : {sumar_arg(a,b)}')

operacion(2,1,sumar)

#3retornar la funcion

def retornar_funcion():
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'{mi_funcion_retornada(50,50)}')