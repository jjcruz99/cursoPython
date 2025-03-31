from exepciones_propias import Numeros_Identicos_Excep

try:
    10/0
except ZeroDivisionError as e: #clase hija solo captura el error cuando se divide por 0
    print(f'Ocurrio un error: {e}')

resultado = None
a = 12
b = '0'
try:
    resultado = a/b
except Exception as e:#clasepadre Exception
    print(f'Ocurrio un error: {e}')

print(f'Resultado = {resultado}')

print('\n       Exepciones especificas ')
try:
    a = int(input("Digite un numero : "))
    b = int(input("Digite un numero : "))
    if a == b:
        raise Numeros_Identicos_Excep('Numeros iguales') #raise lansa una expcion en este caso la ejecuta la Clase Exeption por que es la padre
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrio un error no se puede dividir por  0: {e}')
except TypeError as e:
    print(f'Ocurrio un error  valor no numerico: {e}')
except Exception as e:
    print(f'Error : {e}')
else:
    print("No ocurrio ningun Error")
finally:
    print("Siempre se va a ejecutar - FIN EXEPCIONES")

print(f'Resultado = {resultado}')