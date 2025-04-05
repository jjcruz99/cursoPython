
import os

class CatalogoPeliculas():

    #atributo de clase
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls,pelicula):
        try:
            with open(cls.ruta_archivo,'a',encoding='UTF8') as archivo:
                archivo.write(f'{pelicula.id_pelicula}) {pelicula.nombre}\n')
        except Exception as e:
            print("No se pudo agregar la pelicula por : "+e)

    @classmethod
    def listar_peliculas(cls):
        try:
            with open(cls.ruta_archivo,'r',encoding='UTF8') as archivo :
                print('Catalogo de peliculas'.center(50,'*'))
                print(archivo.read())
        except Exception as e:
            print("No se pudo listar peliculas por : "+e)

    @classmethod
    def eliminar_peliculas(cls):
        try:
            os.remove(cls.ruta_archivo)
            print('Se elimino el archivo')
        except Exception as e:
            print("No se pudo eliminar el archivo por : "+e)



