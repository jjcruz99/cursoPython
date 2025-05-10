
#simulacion de sobre carga de constructores
class Carro:

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def crear_carro_vacio(cls):
        return cls(None,None) #llama el metodo init

    @classmethod
    def crear_carro_con_valores(cls, marca,modelo):
        return cls(marca,modelo)

    def __str__(self):
        return f'{self.marca} y {self.modelo}'


carro1 = Carro('Mazda',2010)
carro_vacio = Carro.crear_carro_vacio()
carro2 = Carro.crear_carro_con_valores('Ferrari',2025)
print(carro1.__str__())
print(carro_vacio.__str__())
print(carro2.__str__())

