#definir la clase
class Persona:

    #metodo de la clase persona
    def inicializar_persona(self,nombre,apellido):
        #atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''
        Nombre: {self.nombre}
        Apellido: {self.apellido} ''')

#creacion de objetos
if __name__ == '__main__':

    persona1 = Persona()#objeto vacio
    persona1.inicializar_persona('John','Cruz')#asignar atributos al objeto
    persona1.mostrar_persona()

    persona2 = Persona()
    persona2.inicializar_persona('Ian','Vargas')
    persona1.mostrar_persona()
