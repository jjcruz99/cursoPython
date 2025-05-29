from usuario import Usuario
from logger_base import log
from cursor_pool import CursorDelPool

class UsuarioDAO:

    #atributos de clase
    _SELECT = 'SELECT * FROM usuarios ORDER BY id_usuario ASC'
    _INSERT = 'INSERT INTO usuarios(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s,password=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            #lista de usuarios tipo usario
            lista_usuarios = []
            for registro in registros:
                usuario1 = Usuario(registro[0],registro[1],registro[2])
                lista_usuarios.append(usuario1)
            return lista_usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            print(f'Usuario a insertar {usuario.__str__()}')
            valores =(usuario.usermane,usuario.password)
            cursor.execute(cls._INSERT,valores)
            log.debug(f'Usuario insertado con EXITO')
            return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.usermane,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Usuarion con id:{usuario.id_usuario} actualizado con exito')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,id):
        with CursorDelPool() as cursor:
            cursor.execute(cls._DELETE,id)
            log.debug(f'Se elimino el usuario con id:{id}')
            return cursor.rowcount

#pruebas
if __name__ == '__main__':

    lista_usuarios = UsuarioDAO().seleccionar()
    print('Usuarios almacenados en la base de datos')
    for usuario in lista_usuarios:
        print(usuario.__str__())

    # usuario1 = Usuario(username='julian',password='12542')
    # usuario_insertado = UsuarioDAO.insertar(usuario1)
    # print(usuario_insertado)

    # usuario2 = Usuario(id_usuario=4,username='Mariela',password='0000')
    # usuario_actualizado = UsuarioDAO.actualizar(usuario2)
    # print(f'Usuarios insertados : {usuario_actualizado}')

    # usuario_eliminado = UsuarioDAO.eliminar('4')
    # print(f'Usuarios insertados : {usuario_eliminado}')