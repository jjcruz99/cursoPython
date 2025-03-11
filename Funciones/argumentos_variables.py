
print("Argumentos variables")
# *args - argumentos - tupla

def diferentes_valores (dato1,dato2, *args):
    print(f'Parametros : {dato1} - {dato2} {args} \n')
    for datos in args:
        print("Iterar los argumentos variables : ",datos)

diferentes_valores("Hola",234,"Datos","Mas datos")

# ++kargs (key, value)
def diferentes_valores_dicc (nombre, *args, **kwargs):
    print(f'{nombre} - {args} - mas info : {kwargs}')

#llammando la funcion
diferentes_valores_dicc("Shailo","Perro","Enano",edad = 6,vacunas=True)
# se puede omitir los args o los kwargs

#funbcionm suma de argumentos
print("Funcion sumar argumentos variables")
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return  total

print(sumar(2,2,2,2))

print("Funcion para recivir multiples diccionarios------------")
def recibir_diccionarios(**kwargs):
    print("\nValores diccionario")
    for llave,valor in kwargs.items():
        print(f'LLave : {llave},valor : {valor} ')

recibir_diccionarios(nombre='Shailo',edad=6,color="Rojito")
recibir_diccionarios(moto="Suzuki",modelo="2024",referencia="Gixxer",cc=250)