from turtledemo.penrose import start


class Coche2:
    def __init__(self, marca=None, modelo=None, color=None):
        self._marca = marca  # atributo publico
        self._modelo = modelo  # atributo protegido
        self._color = color  # atributo privado

    def conducir(self):
        print(f'''
                Conduciendo el coche 
                Marca: {self._marca}
                Modelo: {self._modelo}
                Color: {self._color}
                      ''')

    ####Getters y setters
    @property ##Definir el metodo get
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


if __name__ == '__main__':
    # craer el primer coche
    coche1 = Coche2('Ford', 'Mustang', 'Negro')
    coche1.conducir()

    coche1.marca = 'Chevrolet'
    coche1.modelo = 'Camaro'
    coche1.color ='Negro 2'
    coche1.conducir()
    print(coche1.marca)

    print("\n Atributro dinamico en objetos")
    coche2 = Coche2('Mazda','RX7','Rojo')
    setattr(coche2,'nuevo_atributo', 'Valor nuevo atributo') #Este nuevo atributo solo aplica para este objeto
    coche2.nuevo_atributo2 = 'Valor2 nuevo atributo'
    print(coche2.nuevo_atributo) #se puede imprimir debido al dinamismo de python
    print(f'Obtener todos los atributos de un objeto coche2: {coche2.__dict__}')
