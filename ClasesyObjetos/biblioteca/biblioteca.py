from ClasesyObjetos.biblioteca.libro import Libro

class Biblioteca:

    #atributo de clase
    cantidad_librerias = 0

    #constructor
    def __init__(self,nombre):
        self._nombre = nombre
        self._libros = []

    #metodo de clase
    @classmethod
    def get_cantidad_libros(cls):
        return Biblioteca.cantidad_librerias

    #metodos
    def agregar_libros(self,titulo,autor,genero):
        nuevo_libro = Libro(titulo=titulo,autor=autor,genero=genero)
        self._libros.append(nuevo_libro)

    def mostrar_todos_libros(self):
        for contador,libro in enumerate(self._libros):
            print(f'\n{contador}) {libro.titulo} , {libro.autor}, {libro.genero}')


    def buscar_libros_autor(self,autor):
        verificacion = False
        for libro in self._libros:
            if libro.autor == autor:
                print(f'\n{libro.titulo} , {libro.autor}, {libro.genero}')
        if not verificacion:
            print('No se encontro ningun libro')

    def buscar_libros_genero(self,genero):
        verificacion = False
        for libro in self._libros:
            if libro.genero == genero :
                print(f'\n{libro.titulo} , {libro.autor}, {libro.genero}')
                verificacion = True
        if not verificacion:
            print('No se encontro ningun libro')

    def buscar_libros_titulo(self,titulo):
        verificacion = False
        for libro in self._libros:
            if libro.titulo == titulo :
                print(f'\n{libro.titulo} , {libro.autor}, {libro.genero}')
                verificacion = True
        if not verificacion :
            print('No se encontro ningun libro')

    #getters y setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def libros(self):
        return self._libros

    @libros.setter
    def libros(self,libros):
        self._libros = libros