from herencia_multiple.color import Color
from herencia_multiple.figura_geometrica import Figura_Geometrica


class Rectangulo (Figura_Geometrica,Color) :
    #pass
    def __init__(self,ancho,alto,color):
        Figura_Geometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)

    def __str__(self):
        return f' {Figura_Geometrica.__str__(self)} {Color.__str__(self)}'

    def calcular(self):
        return f'Area rectangulo : {self._alto} * {self._ancho}'
