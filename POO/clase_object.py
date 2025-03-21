class Persona :

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #sobre escribir el metodo __str__
    # si no se sobreescribe imprime la dirrecion de memoria del metodo
    def __str__(self):
        return f''' Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir.Mem = {super.__str__(self)}''' ##acceder a la dirrecion de memoria en la clase padre


#codigo principal
if __name__ == '__main__' :
    persona1 = Persona('Ana', 'Gomez')
    print(persona1) ## se llama de manera automatica el  metodo __str___
    print("Otra forma llamar el metodo __str__")
    print(persona1.__str__()) #es otra opcion

