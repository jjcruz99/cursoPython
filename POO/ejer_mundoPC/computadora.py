from POO.ejer_mundoPC.contador_ratones import Raton
from POO.ejer_mundoPC.monitor import Monitor
from POO.ejer_mundoPC.teclado import Teclado


class Computadora:

    contador_computadora = 0

    #constructor
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f''' Computadora : {self._nombre}
        ID : {self._id_computadora}
        Monitor : ({self._monitor})
        Teclado : ({self._teclado})
        Raton : ({self._raton})
        '''

    #metodo de clase
    @classmethod
    def get_contador_computadora(cls):
        return cls.contador_computadora

    #getters y setters
    @property
    def id_computadora(self):
        return self._id_computadora

    @id_computadora.setter
    def id_computadora(self,id_computadora):
        self._id_computadora = id_computadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self,monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self,teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._teclado

    @teclado.setter
    def raton(self,raton):
        self._raton = raton

##prueba local
if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('Samsung', '27"')
    teclado1 = Teclado('Accer', 'USB')
    computadora1 = Computadora('Nitro',monitor1,teclado1,raton1)

    print(computadora1)