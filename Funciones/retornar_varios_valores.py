
def mayusculas(parametro1,parametro2):
    print("Esta funcion regresa varios valores (Tupla)")
    return parametro1.upper(), parametro2.upper()


tupla_mayusculas = mayusculas("hola","mundo")
print("\n",tupla_mayusculas)
#unpacking de tuplas
argumento1,argumento2 = mayusculas("hola","todos")
print(f"Palabras mayusculas {argumento1} y {argumento2}")