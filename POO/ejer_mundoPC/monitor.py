
class Monitor:

    contador_monitor = 0

    def __init__(self,marca,tamanio):
        self._marca = marca
        self._tamanio = tamanio
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor

    def __str__(self):
        return f'''
        ID : {self._id_monitor}
        Marca : {self._marca}
        Tamaño : {self._tamanio}
        '''

    #metodo de clase
    @classmethod
    def get_contador_monitores(cls):
        cls.contador_monitor

    #getters y setters
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def tamanio(self):
        self._tamanio

    @tamanio.setter
    def tamanio(self,tamanio):
        self._tamanio = tamanio

    @property
    def id_monitor(self):
        return self._id_monitor

    @id_monitor.setter
    def id_monitor(self,id_monitor):
        self._id_monitor = id_monitor

##pruebas en la clase
if __name__ == '__main__':
    monitor1 = Monitor('Samsung' , '27"')
    print(monitor1)

    monitor2 = Monitor('Lenovo' , '24"')
    print(monitor2)
