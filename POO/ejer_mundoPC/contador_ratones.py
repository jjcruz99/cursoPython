from POO.ejer_mundoPC.dispositivo_entrada import Dispositivo_Entrada


class Raton(Dispositivo_Entrada,):

    #atributo de clase
    contador_ratones = 0

    def __init__(self,marca,tipo_entrda):
        Raton.contador_ratones += 1
        self._id_raton =  Raton.contador_ratones
        # self._marca = marca
        # self._tipo_entrda = tipo_entrda
        super().__init__(marca,tipo_entrda) #reutilizar el constructor de la clase padre

    def __str__(self):
        return f'''
        ID : {self._id_raton}
        Marca : {self._marca} 
        Tipo : {self._tipo_entrada}
        ''' #se accede a atributos heredados como propios

    #metodo de clase
    @classmethod
    def get_id_ratones(cls):
       return cls.contador_ratones

    #gettesr y setters

    @property
    def id_raton(self):
        return self._id_raton

    @id_raton.setter
    def id_raton(self,id_raton):
        self._id_raton =id_raton


if __name__ == '__main__':
    raton1 = Raton('HP','USB')
    print(raton1)
    raton2 = Raton('HP','USB')
    print(raton2)
