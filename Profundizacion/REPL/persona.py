class Persona:

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre : {self.nombre} Apellido : {self.apellido}, dir_mem: {hex(id(self))}'

if __name__ == '__main__':
    persona1 = Persona('Juan','Suarez')
    print(persona1)
