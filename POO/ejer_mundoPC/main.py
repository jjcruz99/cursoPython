from POO.ejer_mundoPC.computadora import Computadora
from POO.ejer_mundoPC.contador_ratones import Raton
from POO.ejer_mundoPC.monitor import Monitor
from POO.ejer_mundoPC.orden import Orden
from POO.ejer_mundoPC.teclado import Teclado


raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Samsung', '27"')
teclado1 = Teclado('Accer', 'USB')
computadora1 = Computadora('A320', monitor1, teclado1, raton1)

raton2 = Raton('Accer', 'Bth')
monitor2 = Monitor('Accer', '24"')
teclado2 = Teclado('Accer', 'USB')
computadora2 = Computadora('Nitro', monitor1, teclado1, raton1)

#crear orden
computadores = [computadora1,computadora2]
pedido1 = Orden(computadores)
print(pedido1)

raton3 = Raton('Lenovo', 'Bth')
monitor3 = Monitor('Lenovo', '32"')
teclado3 = Teclado('Lenovo', 'USB')
computadora3 = Computadora('Gamer', monitor1, teclado1, raton1)

pedido1.agregar_computadora(computadora3)
print(pedido1)
