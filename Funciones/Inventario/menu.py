from agregar_producto import agregar_producto
from mostrar_producto import mostrar_todo
from eliminar import eliminar_producto_id
from tamanio import tamanio_inventario
def menu():
    inventario = []
    while(True):
        print("""\n Opciones 
         1) Agregar producto
         2) Eliminar producto
         3) Obtener todos los productos
         4) Obtener tamaño del inventario
         5) Salir
           """)
        opcion = int(input("Digite una opcion 1,2..5 : "))
        match(opcion):
            case 1:
                print("   Agreagar producto ")
                inventario.append(agregar_producto())
            case 2:
                print("   Eliminar producto" )
                inventario = eliminar_producto_id(inventario)
            case 3:
                print("   Obtener el total de productos")
                mostrar_todo(inventario)
            case 4:
                print("    Tamaño del inventario")
                tamanio_inventario(inventario)
            case 5:
                print("    ****** Fin del programa")
                break
            case _:
                print("Digite una opcion valida")