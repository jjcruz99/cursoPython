class Encapsulamiento_coche:

    def __init__(self,marca,modelo,color):
        self.marca = marca #atributo publico
        self._modelo = modelo #atributo protegido
        self.__color = color #atributo privado

    def conducir(self):
        print(f'''
        Conduciendo el coche 
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}
              ''')

if __name__ == '__main__':
    #craer el primer coche
    coche1 = Encapsulamiento_coche('Ford','Mustang','Negro')
    coche1.conducir()

    coche1.marca = 'Chevrolet'
    coche1._modelo = 'Camaro' ## No es una buena practica
    coche1._Encapsulamiento_coche__color = 'Negro 2'## No es una buena practica
    coche1.conducir()