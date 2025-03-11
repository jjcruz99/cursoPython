
id = 0
def agregar_producto():
    global  id
    id += 1
    nombre=input("Digite el nombre del producto: ")
    precio = float(input("Digite el precio del producto: "))
    cantidad = int(input("Digite la cantidad de unidades: "))
    producto = {
        'id':id ,
        'nombre':nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    return producto