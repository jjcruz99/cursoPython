
class Cliente:

#constructor
    def __init__(self,id_cliente=None,nombre=None,apellido=None,membresia=None):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia

    def __str__(self):
        return (f'ID: {self._id_cliente} , Nombre: {self._nombre}',
                f'Apellido: {self._apellido}, Membresia: {self._membresia}')


    ##getters y setters

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self,id):
        self._id_cliente = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return  self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def membresia(self):
        return self._membresia

    @membresia.setter
    def membresia(self,membresia):
        self._membresia = membresia


if __name__ == '__main__':

    cliente1 = Cliente(nombre='John',apellido='Ariza',membresia=2563)
    print(cliente1.__str__())
    cliente1.nombre = 'Gato'
    print(cliente1.__str__())