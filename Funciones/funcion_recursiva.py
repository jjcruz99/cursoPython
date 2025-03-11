
print("           Funcion recursiva \n")

def funcion_recursiva(numero):
    if numero == 1:
        print(numero, end=" ")
    else:# llamar funcion recursiva
        #print(numero,end= ' ') #desendente
        funcion_recursiva(numero - 1)##la funcion debe terminar
        print(numero,end= ' ') ## se imprime hasta finalizar todas las llamadas recursivas

## factorial de un numero
def funcion_recursiva_factorial(numero):
    if numero == 0 or numero==1:
        return  1
    else :
        factorial = numero * funcion_recursiva_factorial(numero - 1)
        return factorial

#factorial de todos los numeros hasta n
def funcion_recursiva_factoriales(numero2):
    if numero2 == 0 or numero2==1:
        print(f'{numero2}! = 1')
        return  1
    else :
        factorial2 = numero2 * funcion_recursiva_factoriales(numero2 - 1)
        print(f'{numero2}! = {factorial2}')
        return factorial2


if __name__ == '__main__':
    funcion_recursiva(5)

    #llamar funcion factorial
    factorial = funcion_recursiva_factorial(5)
    print(f'\n5! = {factorial}')

    #llamar funcion factoriales
    numero = int(input("Digite un numero: "))
    resultado = funcion_recursiva_factoriales(numero)
    print(f'El factorial del numero {numero} = {resultado}')