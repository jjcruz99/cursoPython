from herencia_multiple.color import Color
from herencia_multiple.figura_geometrica import Figura_Geometrica

class Cuadrado(Figura_Geometrica , Color): ## hereda de dos clases padres

    def __init__(self,lado,color):
        #inicializa los parametros de la clase
       Figura_Geometrica.__init__(self,lado,lado)
       Color.__init__(self,color)

    def __str__(self):
        return f'{Figura_Geometrica.__str__(self)} {Color.__str__(self)}'

    def calcular(self):
        return  f' Area cuadrado: {self.alto} * {self.ancho}'


if __name__ == '__main__':
    #metodo de orden de resolucion mro()
    print(Cuadrado.mro())