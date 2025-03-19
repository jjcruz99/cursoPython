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


