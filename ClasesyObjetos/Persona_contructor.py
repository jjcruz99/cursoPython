class Persona_constructor:

    #constructor
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        print(f'''
         Nombre : {self.nombre}
         Apellido : {self.apellido} ''')
        print(f'Dir self : {id(self)}')#Direccion de memoria

if __name__ == '__main__':

    persona1 =  Persona_constructor('Camila','Diaz')
    persona1.mostrar()
    print(f'Direccion de memoria de persona1 {id(persona1)}')
    print(f'Direccion HEX de memoria de persona1 {hex(id(persona1))}')

    persona2 = Persona_constructor('Ana', 'Sanchez')
    persona2.mostrar()