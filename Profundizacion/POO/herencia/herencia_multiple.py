
class ManejoLista:

    def __init__(self, elementos):
        self._elemntos = list(elementos)

    def agregar(self,elemento):
        self._elemntos.append(elemento)

    def __getitem__(self, item):
        return  self._elemntos[item]

    def ordenar(self):
        return  self._elemntos.sort()

    def __len__(self):
        return len(self._elemntos)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._elemntos})'



class ListaOrdenada(ManejoLista):

    def __init__(self, elementos=[]):
        super().__init__(elementos)
        self.ordenar()

    def agregar(self,elemento):
        super().agregar(elemento)
        self.ordenar()



class ListaEnteros(ManejoLista):

    def __init__(self, elementos):
        for elemento in elementos:
            self._validar(elemento)

        super().__init__(elementos)

    def _validar(self,elmento):
        if not isinstance(elmento,int):
            raise  ValueError(f'No es entero {elmento}')

    def agregar(self,elemento):
        self._validar(elemento)
        super().agregar(elemento)



class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


if __name__ == "__main__":

    lista_simple1 = ManejoLista([5,6,9,36,47,51,59,53,57])
    print(lista_simple1)

    lista_ordenada1 = ListaOrdenada([5,6,9,36,47,51,59,53,57])
    print(lista_ordenada1)
    lista_ordenada1.agregar(-58)
    print(lista_ordenada1)
    print(lista_ordenada1.__len__())

    print('\nLista de enteros')
    lista_enteros1 = ListaEnteros([1,56,5,23])
    print(lista_enteros1)

    print('\nLista de enteros ordenada Herencia Multiple')
    lista_enteros_ordenada1 = ListaEnterosOrdenada([1, 56, 5, 23,-9,58,-1000])
    print(lista_enteros_ordenada1)

    print('\nSaber el orden de las clases')
    print(ListaEnterosOrdenada.__bases__)
    print(f'MRO {ListaEnterosOrdenada.__mro__}')


    print('Uso isinstance? '.center(60,'*'))
    print('Es entero? ',isinstance(25,int))
    print('Es String? ',isinstance('Hola',str))
    print('Es listaEntero?',isinstance(lista_enteros1,ListaEnteros))
    print('Es listaEnteroOrdenada? ',isinstance(lista_enteros_ordenada1,ListaEnterosOrdenada))
    print('Es de varios tipos?',isinstance(lista_enteros1,(ListaEnteros,ListaEnteros,object)))




