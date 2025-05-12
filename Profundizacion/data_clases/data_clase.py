from dataclasses import dataclass
from typing import ClassVar

# https://docs.python.org/3/library/dataclasses.html

#frozen hace que las instancias de la clase sean inmutables
@dataclass(eq=True, frozen=True)
class Domicilio:
    calle : str
    numero : int = 0


#decorador
@dataclass(eq=True, frozen=True) #frozen hace que las instancias de la clase sean inmutables
class Persona: #

    nombre : str
    apellido :str
    contador_persona: ClassVar[int] = 0
    domicilio : Domicilio
    def __post_init__(self):
        if not self.nombre:
            raise  ValueError ('valor del nombre no puede estar vacio')

domicilio1 = Domicilio('caracas',20)
persona1 = Persona('Juan','Perez',Domicilio('caracas',20))
print(persona1)
print(f'{persona1!r}') #llamando al metodo __repr__

print(f'Varaiable de clase {persona1.contador_persona}')
print(f'Variebles de isntancia {persona1.__dict__}')

persona_vacia = Persona("jaime","",Domicilio('boyaca',20))
print(persona_vacia)

#revisar igualdad entre objetos
persona2 = Persona('Juan','Perez',domicilio1)

print(f'\nObjetos son iguales : {persona2 == persona1}')

#Agregar esta clase a una coleccion
coleccion = {persona1,persona2}