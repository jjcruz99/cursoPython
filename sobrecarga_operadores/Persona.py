
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    #sobrecarga de operadores
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


if __name__ == '__main__':

    object1 = Persona('John' , 32)
    object2 = Persona('Camila' , 25)

    print(object1 + object2)#utiliza la sobrecarga del metodo __add__
    print(object1 - object2)


