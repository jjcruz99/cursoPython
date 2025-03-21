class Dispositivo_Entrada :

    def __init__(self,marca,tipo_entrda):
        self._marca = marca
        self._tipo_entrada = tipo_entrda

    #getters y setters
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrda(self,tipo_entrada):
        self._tipo_entrada = tipo_entrada

