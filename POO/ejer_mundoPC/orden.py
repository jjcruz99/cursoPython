
class Orden:

    contador_ordenes = 0

    def __init__(self,lista_pedidido):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._lista_pedido = lista_pedidido

    def agregar_computadora(self,computadora):
        self._lista_pedido.append(computadora)
        print('\nSe agrego una computadora con exito')

    def __str__(self):
        computadores_str = ''
        for computador in self._lista_pedido:
            computadores_str += computador.__str__()

        return f''' orden {self._id_orden}
        detalles del pedido
        {computadores_str}
         '''







