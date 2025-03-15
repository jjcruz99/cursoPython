
class Aritmetica:

    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        print(f'Suma = {self.numero1 + self.numero2}')

    def multiplicar(self):
        print(f'Producto = {self.numero1 * self.numero2}')

    def restar(self):
        print(f'resta = {self.numero1 - self.numero2}')

    def dividir(self):
        if self.numero2 > 0 :
             print(f'Dividir = {self.numero1 / self.numero2}')
        else:
            print("No es posible dividir por 0 ")