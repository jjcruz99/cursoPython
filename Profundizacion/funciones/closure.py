
#Es una funcion que define a otra

def operacion(a,b):

    def sumar():
        return a+b
    #retornar la funcion
    return sumar

mi_funcion_closure = operacion(5,2)
print(mi_funcion_closure())

print(f'Resultado {operacion(6,9)()}')

def calcular(c,d):
    return lambda : c + d

print(f'Resultado {calcular(100,900)()}')
