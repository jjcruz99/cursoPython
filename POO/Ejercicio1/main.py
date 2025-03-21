from POO.Ejercicio1.gato import Gato
from POO.Ejercicio1.herencia import Animal
from POO.Ejercicio1.metodo_polimorfico import dormir_animal
from POO.Ejercicio1.perro import Perro

print("Ejemplo de herencia en Python")
print("\n         Objeto de la clase padre Animal")

animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\n          Objeto de clase hija Perro')
perro1 = Perro()
perro1.dormir() # se realizo sobreescritura del metodo en clase hija
perro1.comer()
perro1.hacer_sonido()##metodo propio de la clase

print('\n  Objeto de la clase hija Gato')
gato1 = Gato()
gato1.dormir() #Pilimorfismo realizo herencia y sobre escritura del metodo agregando sus propios comportamiento del gato

print('\n  Objeto de la clase hija Gato usando metodo polimorfico')
gato2 = Gato()
#utilizar metodo polimorfico
dormir_animal(gato2)