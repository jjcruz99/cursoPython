class Libro:

    contador_libros = 0

    def __init__(self,titulo=None,autor=None,genero=None):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        Libro.contador_libros += 1

    @classmethod
    def get_contador_libros(cls):
        return cls.contador_libros

    ##getters y setters
    @property
    def titulo(self):
        return  self._titulo

    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self,autor):
        self._autor = autor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self,genero):
        self._genero = genero


