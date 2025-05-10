
#es unba funcion que ricebe y regresa otra funcion

# def funcion_decorador(mostrar_mensaje_aDecorar):
#     def funcion_decorada():
#         print('      Antes de ejecutar la funcion')
#         mostrar_mensaje_aDecorar()
#         print('      Despues de ejecutar la funcion')
#
#     return funcion_decorada
#
# @funcion_decorador
# def mostrar_mensaje():
#     print('Hola desde fun mostrar mensaje')
#
# mostrar_mensaje()

def funcion_decorador(mostrar_mensaje_aDecorar):
    def funcion_decorada(*args, **kwargs):
        print('      Antes de ejecutar la funcion')
        resultado = mostrar_mensaje_aDecorar(*args, **kwargs)
        print('      Despues de ejecutar la funcion')
        return resultado

    return funcion_decorada

@funcion_decorador
def sumar(a,b):
    return a+b

resultado = sumar(5,5)
print(resultado)