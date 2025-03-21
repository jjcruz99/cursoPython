from POO.ejer_mundoPC.dispositivo_entrada import Dispositivo_Entrada

#La clas teclado hereda de la clase padre Dispositivo_Entrada
class Teclado(Dispositivo_Entrada):

    #atributo de clase
    contador_teclado =0

    #constructror heredado
    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f'''
        ID : {self._id_teclado}
        Marca : {self._tipo_entrada}
        Tipo de entrada : {self._tipo_entrada}
        '''

    ## getters y setters
    @property
    def id_teclado(self):
        return self._id_teclado

    @id_teclado.setter
    def id_teclado(self,id_teclado):
        self._id_teclado = id_teclado


if __name__ == '__main__' :
    teclado1 = Teclado('Accer','USB')
    print(teclado1)