print("   Mi primera funcion \n")
#funcion sin parametros
def saludar():
    print("Hola desde la funcion")

saludar()#llamar la funcion

##funcion con parametros
def saludar2(nombre):
    return  f'Hola {nombre} desde la funcion 2 '

saludo = saludar2("John") #llamar la funcion enviar argumento
print(saludo)

print(saludar2("Diana"))##reutilizar la funcion