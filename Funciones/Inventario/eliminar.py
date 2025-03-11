from cgi import print_form


def eliminar_producto_id(invetario_total):
    producto_eliminar = False
    id = int(input("Digite el id del producto que desea eliminar: "))
    for posicion,producto in enumerate(invetario_total):
        if producto.get('id') == id :
            producto_eliminar = True
            invetario_total.pop(posicion)
    mensaje ='No se encontro ningun producto' if producto_eliminar == False else '**** Se elimino el producto del inventario.'
    print(mensaje)
    return invetario_total

