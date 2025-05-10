#representacion de un objeto
#print(dir(object))
class Animal:
    '''
    Clase Animal prueba para representar objetos
    '''
    def __init__(self,especie,nombre):
        '''
        :param especie:
        :param nombre:
        '''
        self.especie = especie
        self.nombre = nombre


    def __repr__(self):
        '''
        :return: los atributos
        '''
        return f'{self.__class__.__name__}(especie:{self.especie}, nombre:{self.nombre})'

    #str esta orientado al usuario final
    def __str__(self):
        return f'{self.__class__.__name__}({self.especie},{self.nombre})'

    #Por default es el str
    def __format__(self, format_spec):
        return f'{self.__class__.__name__}su especie es : {self.especie}, con nombre{self.nombre})'




if __name__ == '__main__':
    animal1 = Animal('Felino','Tigre')
    print(f'{animal1!r}')#llamar el metodo  repr
    print(f'{animal1}')##llamado str
    print(f'{animal1}')##llamado format al usar un f''

    help(Animal)