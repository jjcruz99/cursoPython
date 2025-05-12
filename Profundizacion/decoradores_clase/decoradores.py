import inspect


def decorador_repr(cls):
    print('Se ejecuta decorador')
    print(f'Recibimos objeto tipo : {cls.__name__}')
    #Revisar los atributos de la clase
    atributos = vars(cls)
    # for nombre, atributo in atributos.items():
    #     print(nombre,atributo)

    #revisar si se ha sobreescrito el metodo __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__}')

    #recuperar la firma
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__ : {firma_init}')

    #recuperamos los parametros menos self
    parametros_init = list(firma_init.parameters)[1:]
    print(parametros_init)

    #Revisar si cada parametro tiene un metodo property
    for parametro in parametros_init:
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe u metodo property para el parametro: {parametro}')

    #crear metodo repr dinamicamente
    def metodo_repr(self):
        nombre_clase = self.__class__.__name__
        print(f'Nombre de la clase : {nombre_clase}')

        generdador_arg = (f'{nombre}={getattr(self,nombre)!r}' for nombre in parametros_init)
        lista_arg = list(generdador_arg)
        print(f'Lista del generador {lista_arg}')

        return f'Metodo repr'

#   Cuando se manda llmar el metodo repr se llama automaticamente el metodo_repr
    setattr(cls,'__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:

    def __init__(self,nombre, apellido):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido


    @property
    def nombre(self):
        return self.nombre

    @property
    def apellido(self):
        return self._apellido

    #def __repr__(self):


persona1 = Persona('juan','cruz')
print(persona1)