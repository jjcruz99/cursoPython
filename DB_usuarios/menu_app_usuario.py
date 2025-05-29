from cursor_pool import CursorDelPool
from logger_base import log
from usuario import Usuario
from usuarioDAO import UsuarioDAO

print(' Programa gestion DB de usuarios '.center(50,'*'))
opcion = 0
while True:
    print('\nMenu : Digite una opcion(1,2..)'.center(30,'-'))
    print('''1) Mostrar todos los usuarios
2) Insertar un usuario
3) Actualizar usuario
4) Eliminar usuario
5) Salir ''')

    opcion = int(input(":"))
    match opcion :
        case 1:
            lista_usuarios = UsuarioDAO().seleccionar()
            print('Usuarios almacenados en la base de datos')
            for usuario in lista_usuarios:
                print(usuario.__str__())
        case 2:
            username = input('Digite el nombre del usuario: ')
            password = input('Digite el password: ')
            usuario1 = Usuario(username=username,password=password)
            usuario_insertado = UsuarioDAO.insertar(usuario1)
            print('Usuario insertado con exito') if usuario_insertado == 1 else print('No se inserto el usuario')
        case 3:
            id_usuario = input('Digite el id_usuario: ')
            username = input('Digite el nombre del usuario: ')
            password = input('Digite el password: ')
            usuario1 = Usuario(id_usuario=id_usuario,username=username, password=password)
            usuario_actualizado = UsuarioDAO.actualizar(usuario1)
            print('Usuario actualizado con exito') if usuario_actualizado == 1 else print('No se actualizado el usuario')
        case 4:
            id = input('Digite el id_usuario: ')
            usuario_eliminado = UsuarioDAO.eliminar(id)
            print('Usuario eliminado con exito') if usuario_eliminado == 1 else print('No se eliminado el usuario')
        case 5:
            print('\nFin del programa')
            break #sale del while
        case _:
            print('\nDigite una opcion valida')