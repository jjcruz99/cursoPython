# Instrucciones
# Escribe un programa que tome dos números de entrada, luego los sume e imprima el resultado.
#
# **Recuerda** Este proyecto se calificará automáticamente, ¡y las computadoras son muy literales!
#
# ## Tiempo adicional
#
# Si completas esta tarea, intenta agregar las siguientes funciones:
# * Toma dos números y resta el segundo del primer número.
# * Toma dos números y multiplica los dos.
# * Toma dos números y divide el primer número por el segundo número.
# * Toma dos números y realiza una operación de módulo.
# * Permite que los usuarios elijan qué operación desean realizar con dos números.
# * Toma 3 números y súmalos.
# * Permite que los usuarios mezclen operaciones con 3 números o más
# p. ej. 2 + 4 - 3, 4 *5 + 1 / 3
#
# **Nota:** Estas funciones deben presentarse al usuario *después* de la tarea inicial, o de lo contrario, la calificación automática
# la marcará como reprobada. La puntuación de las funciones adicionales se realizará manualmente.

# num1 = int(input('Digite un numero: '))
# num2 = int(input('Digite un numero: '))
# print(num1 + num2)

###############   Definir las funciones

def ingreso_dos_numeros():
    num1 = int(input('Digite un numero entero: '))
    num2 = int(input('Digite un numero entero: '))
    return num1,num2

def fun_resta(num1,num2):
    resultado = num1 - num2
    return resultado

def fun_multiplicacion (num1,num2):
    resultado = num1 * num2
    return resultado

def fun_division (num1,num2):
    resultado = num1 / num2
    return resultado

def fun_modulo (num1,num2):
    resultado = num1 / num2
    return resultado

def fun_sumar_tres (num1,num2,num3):
    resultado = num1 + num2 + num3
    return resultado

def fun_ecuacion (ecuacion):
    numeros = []
    aritmeticos = []
    resultado = 0
    cantidad_numeros = 0
    #Separar numeros y operadores aritmeticos
    for i in ecuacion :
        if i == '+' or i == '-' or i == '*' or i == '/' or i == '%':
            aritmeticos.append(i)
        else :
            numeros.append(float(i))
            cantidad_numeros += 1 ##obtener la cantidad de numeros


    while cantidad_numeros > 1:
        ##realizar productos
       indice = 0
       reinicio = False
       while indice < cantidad_numeros - 1:
           i = aritmeticos[indice]
           if i == '*' :
               resultado = numeros[indice] * numeros[indice + 1]
               numeros[indice] = resultado
               numeros.pop(indice + 1)
               aritmeticos.pop(indice)
               cantidad_numeros -= 1
               reinicio = True
           indice += 1
           if reinicio == True:
               indice = 0
               reinicio = False

     ##realizar divisiones
       indice = 0
       while indice < cantidad_numeros - 1:
           i = aritmeticos[indice]
           if i == '/':
               resultado = numeros[indice] / numeros[indice + 1]
               numeros[indice] = resultado
               numeros.pop(indice + 1)
               aritmeticos.pop(indice)
               cantidad_numeros -= 1
               reinicio = True
           indice += 1
           if reinicio == True:
               indice = 0
               reinicio = False

     ##realizar modulos
       indice = 0
       while indice < cantidad_numeros - 1:
           i = aritmeticos[indice]
           if i == '%':
               resultado = numeros[indice] % numeros[indice + 1]
               numeros[indice] = resultado
               numeros.pop(indice + 1)
               aritmeticos.pop(indice)
               cantidad_numeros -= 1
               reinicio = True
           indice += 1
           if reinicio == True:
               indice = 0
               reinicio = False

     ##realizar sumas
       indice = 0
       while indice < cantidad_numeros - 1:
           i = aritmeticos[indice]
           if i == '+':
               resultado = numeros[indice] + numeros[indice + 1]
               numeros[indice] = resultado
               numeros.pop(indice + 1)
               aritmeticos.pop(indice)
               cantidad_numeros -= 1
               reinicio = True
           indice += 1
           if reinicio == True:
               indice = 0
               reinicio = False

     ##realizar restas
       indice = 0
       while indice < cantidad_numeros - 1:
           i = aritmeticos[indice]
           if i == '-':
               resultado = numeros[indice] - numeros[indice + 1]
               numeros[indice] = resultado
               numeros.pop(indice + 1)
               aritmeticos.pop(indice)
               cantidad_numeros -= 1
               reinicio = True
           indice += 1
           if reinicio == True:
               indice = 0
               reinicio = False

    return numeros[0]



###Seleccionar opcines
opcion = 0
while opcion != 7:
    opcion = int(input(f''' \n       Menu :
    1.Resta
    2.Multiplicacion
    3.Division
    4.Modulo
    5.Sumar tres numeros
    6.Ecuacion (ej. 2+6*8..)
    7.Salir
    Digite una opcion(1-7): 
    '''))

    if opcion == 1: ####resta
        num1,num2 = ingreso_dos_numeros()
        resultado = fun_resta(num1,num2)
        print (resultado)

    elif opcion == 2: ####multiplicacion
        num1,num2 = ingreso_dos_numeros()
        resultado = fun_multiplicacion(num1, num2)
        print(resultado)

    elif opcion == 3: ####division
        num1,num2 = ingreso_dos_numeros()
        resultado = fun_division(num1, num2)
        print(resultado)

    elif opcion == 4: ####modulo
        num1,num2 = ingreso_dos_numeros()
        resultado = fun_modulo(num1, num2)
        print(resultado)

    elif opcion == 5: #Sumar tres numeros
        num1 = int(input('Digite un numero entero: '))
        num2 = int(input('Digite un numero entero: '))
        num3 = int(input('Digite un numero entero: '))
        resultado = fun_sumar_tres(num1,num2,num3)
        print(resultado)

    elif opcion == 6:  # ecuacion
        ecuacion = input('Digite la ecuacion: ')
        ecuacion.strip()
        resultado=fun_ecuacion(ecuacion)
        print('Resultado',+ resultado)

    elif opcion == 7:
        print('Hasta pronto')
    else:
        print('Digite una opcion valida')