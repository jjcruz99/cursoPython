class Coche:

    def __init__(self, marca, modelo, color):
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
    def get_marca(self):
        return self._marca

    def set_marca(self,marca):
        self._marca = marca

    def get_modelo(self):
        return  self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return  self._color

    def set_color(self,color):
        self._color = color

if __name__ == '__main__':
    # craer el primer coche
    coche1 = Coche('Ford', 'Mustang', 'Negro')
    coche1.conducir()

    coche1.set_marca('Chevrolet')
    coche1.set_modelo('Camaro')
    coche1.set_color('Negro 2')
    coche1.conducir()
    print(coche1.get_marca())