
print("                    Control de productos")

inventario = []
opcion = 0;

while (True):
    print("""     \nMenu digite una opcion (1,2,3....)
      1) Agregar producto
      2) Eliminar
      3) Buscar por Id
      4) Mostrar todos los productos
      5) Salir :
    """)
    opcion = int(input())
    match opcion:
        case 1:
            id = int(input("Digite id del producto : "))
            nombre = input("Digite el nombre del producto : ")
            precio = float(input("Digite el precio: "))
            cantidad = int(input("Digite la cantidad : "))
            inventario.append({
                'id': id,
                'nombre':nombre,
                'precio': precio,
                'cantidad': cantidad
                })
            print(f'Se agrego el producto con exito : {inventario[len(inventario)-1]}')
        case 2:
            id_eliminar = int(input("Digite el id del producto que desea eliminar : "))
            existe = False
            for indice, producto in enumerate(inventario):
                if producto.get('id') == id_eliminar :
                    inventario.pop(indice)
                    print("Un producto fue eliminado")
                    existe = True
                    break
            if not existe:
                print("El producto no existe")
        case 3:
            id_buscar= int(input("Digite el id del producto que desea buscar : "))
            existe = False
            for indice, producto in enumerate(inventario):
                if producto.get('id') == id_buscar:
                    print(f'Detalles del producto : {producto}')
                    existe = True
                    break
            if not existe:
                print("El producto no existe")
        case 4:
            print("Listando todos los productos")
            for posicion , detalles_producto in enumerate(inventario) :
                print(f'{posicion} ) {detalles_producto}')
        case 5:
            print("Fin del programa")
            break
        case _:
            print("Digite una opcion valida")