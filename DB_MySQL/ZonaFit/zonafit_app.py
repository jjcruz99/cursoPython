from pool_conexion import Conexion
from cliente import Cliente
from clienteDAO import ClienteDAO

print(' Clientes zona Fit '.center(60,'*'))

opcion = None

while True:
    print('''\nMenu
    1)Mostrar todos los clientes
    2)Insertar
    3)Actualizar
    4)Eliminar
    5)Salir''')

    try:
        opcion = int(input('Digite una opcion: '))
    except Exception as e:
        print(f'Digite un valor numerico : {e}')

    match(opcion):
        case 1:
            clientes = ClienteDAO.seleccionar()
            for cliente in clientes:
                print(cliente.__str__())
        case 2:
            nonmbre = input('Digite el nombre: ')
            apellido = input('Digite el apellido: ')
            membresia = int(input('Digite la membresia: '))
            cliente1 = Cliente(nombre=nonmbre, apellido=apellido, membresia=membresia)
            validacion = ClienteDAO.insertar(cliente1)
            print(validacion)
        case 3:
            id= int(input('Digite el id: '))
            nonmbre = input('Digite el nombre: ')
            apellido = input('Digite el apellido: ')
            membresia = int(input('Digite la membresia: '))
            cliente1 = Cliente(id_cliente=id,nombre=nonmbre, apellido=apellido, membresia=membresia)
            validacion = ClienteDAO.actualizar(cliente1)
            print(validacion)
        case 4:
                id = int(input('Digite el id: '))
                validacion = ClienteDAO.eliminar(id)
                print(validacion)
        case 5:
            print('Fin del programa'.center(50,'*'))
            break
        case _:
            print('Digite un valor dentro del rango'.center(40,'-'))

