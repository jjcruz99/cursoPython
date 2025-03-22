class Figura_Geometrica:

    def __init__(self,ancho,alto):
        if ancho > 0 and alto > 0:
            self._ancho = ancho
            self._alto = alto
        else :
            print('Ingrese valores mayores que 0')

    def __str__(self):
        return  f''' Figura Geometrica
        Ancho : {self._ancho}
        Alto : {self._alto}
        '''

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        self._alto = alto