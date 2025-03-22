from herencia_multiple.cuadrado import Cuadrado
from herencia_multiple.rectangulo import Rectangulo

#objeto cuadradado
cuadrado1 = Cuadrado(5,'Rojo')
print(cuadrado1.ancho) # se accede atraves de getters
print(cuadrado1.alto)
print(cuadrado1.calcular())

#objeto rectangulo
rectangulo1 = Rectangulo(5,10,'Amarillo')
print(rectangulo1.color)
print(rectangulo1.calcular())
