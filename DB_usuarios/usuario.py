
class Usuario:

    def __init__(self,id_usuario=None,username=None,password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f''' Usuario:
        id_usuario: {self._id_usuario}
        username: {self._username}
        password: {self._password}'''

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usuario = id_usuario

    @property
    def usermane(self):
        return self._username

    @usermane.setter
    def username(self,username):
        self._username=username

    @property
    def password(self):
        return  self._password

    @password.setter
    def password(self,password):
        self._password=password

if __name__ == '__main__':
    usuario1 = Usuario(username='Jairo',password='cruz125')
    print(usuario1.__str__())

    #borrar la instancia
    del usuario1
    try:
        print(usuario1)
    except Exception as e:
        print(f'Error al intentar acceder al usuario1. Detalles : {e}')