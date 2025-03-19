class Persona :

    atributo_clase = 0 #atributo de clase
    contador_personas = 0

    def __init__(self,atributo_instancia):
        self._atributo_instancia = atributo_instancia
        Persona.contador_personas += 1 #incrementa cada vez se crea un objeto y se asigna al ID
        self._id = Persona.contador_personas

    def mostrar(self):
        print(f'\nDatos de la persona {self._atributo_instancia} id={self._id}')

    @property
    def atributo_instancia(self):
        return  self._atributo_instancia

    #metodos de clase
    @staticmethod
    def get_contador_personas_statico():
        print('Metodo estatico')
        return Persona.contador_personas

    #es el metodo de clase mas recomendado para trabajar atributos de clase
    @classmethod
    def get_contador_personas_clase(cls):
        print('Metodo de clase')
        return cls.contador_personas

if __name__ == '__main__':
    print(' Atributos de clase')
    Persona.atributo_clase = 10 #modificar atributo de clase
    print(f'Atributo de  clase {Persona.atributo_clase}')

    persona1 = Persona("John")
    print(persona1.atributo_clase)
    print('Atributo_instancia :',persona1.atributo_instancia)
    persona1.mostrar()

    persona2 = Persona("Mariela")
    print(persona2.atributo_clase)
    persona2.mostrar()

    ##aceder a los atributos de clase con metodos de clase
    print(f'{Persona.get_contador_personas_statico()}')
    print(f'{Persona.get_contador_personas_clase()}')
