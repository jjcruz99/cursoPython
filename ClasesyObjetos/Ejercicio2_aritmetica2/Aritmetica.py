
class Aritmetica:

    def __init__(self,numero1=None,numero2=None): #Asignar el valor None para poder crear objetos sin parametros iniciales
        self._numero1 = numero1
        self._numero2 = numero2

    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self,numero1):
        self._numero1 = numero1

    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self,numero2):
        self._numero2 = numero2

    def sumar(self):
        print(f'Suma = {self._numero1 + self._numero2}')

    def multiplicar(self):
        print(f'Producto = {self._numero1 * self._numero2}')

    def restar(self):
        print(f'resta = {self._numero1 - self._numero2}')

    def dividir(self):
        if self._numero2 > 0 :
             print(f'Dividir = {self._numero1 / self._numero2}')
        else:
            print("No es posible dividir por 0 ")