
class Padre:

    def __init__(self):
        print('Constructor padre ')

    def metodo(self):
        print('Metodo padre')

class Hija(Padre):
    #de ma nera opcional llamar  __init__ de la clase padre
    def __init__(self):
        super().__init__()
        print('Constructor hija')

   #sobreescribir metodo hereda
    def metodo(self):
       print('Metodo sobreescrito hijo')

hijo1 = Hija()
hijo1.metodo()