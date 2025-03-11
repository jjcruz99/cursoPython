##Funcion para mostrar productos
def mostrar_todo(inventario_total):
    for posicion,producto in enumerate(inventario_total):
        print(f'\n    Producto: {posicion}')
        print(f'-id: {producto.get('id')}')
        print(f'-Nombre: {producto.get('nombre')}')
        print(f'-Precio: {producto.get('precio')}')
        print(f'-Cantidad: {producto.get('cantidad')}')