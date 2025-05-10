
def calculadora(a,b):

    #Definir lla funcion anidada
    def sumar(a,b):
        return a +b

    def restar(a,b):
        return a-b
    #llamar la funcion anidada
    print(sumar(a, b))
    print(restar(a, b))


calculadora(5,6)