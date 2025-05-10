
class Persona:

    contador_personas = 0

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

if __name__ == '__main__':
    persona1 = Persona('Jerjes','Cruz')
    print(persona1.__dict__)

    print(persona1.contador_personas)

    persona1.contador_personas=20#creao otro atibuto del objeto
    print(persona1.__dict__)

    #modificar atributo de clase
    Persona.contador_personas = 10
    print(persona1.contador_personas)

    #atributos de clase al vuelo
    Persona.contador2 = 100
    print(Persona.contador2)
