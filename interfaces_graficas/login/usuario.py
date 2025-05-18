
class Usuario:

    def __init__(self,usuario,clave):
        self._usuario = usuario
        self._clave = clave

    def __str__(self):
        return f'Usuario: {self._usuario} , Clave: {self._clave}'

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self,usuario):
        self._usuario

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self,clave):
        self._clave = clave

