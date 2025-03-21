from POO.Ejercicio1.herencia import Animal


class Perro(Animal): #Clase hija Hereda de la Clase animal

    def hacer_sonido(self):
        print("Gua Gua ")

    #sobrescritura del metodo dormir
    def dormir(self):
        print('Duermo 15 horas al dia')