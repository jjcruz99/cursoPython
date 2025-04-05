from Catalogo_peliculas.Dominio.Pelicula import Pelicula
from Catalogo_peliculas.Servicios.CatalogoPeliculas import CatalogoPeliculas as CP

opcion = 0

while(True):
    print('Menu'.center(40,'-'))
    print('Digite una opcion (1,2..'.center(40,'-'))
    print('''    1). Agregar pelicula
    2). Listar peliculas
    3). Eliminar peliculas
    4). Salir
      : ''')
    try:
        opcion = int(input().strip())
    except Exception as e:
        print('Digite una valor valido')
        print(str(e))

    match(opcion):
        case 1:
            nombre = input('Digite el nombre de la pelicula : ' ).strip()
            if nombre:
                pelicula = Pelicula(nombre)
                CP.agregar_pelicula(pelicula)
            else:
                print("El campo no puede estar vacio")
        case 2:
            CP.listar_peliculas()
        case 3:
            confirmacion = input("Esta seguro de eliminar el archivo (si/no) : ").strip().lower()
            if(confirmacion == 'si'):
                CP.eliminar_peliculas()
            else:
                print("Operación cancelada")
        case 4:
            print("Fin del programa")
            break
        case _:
            print("La opcion fuera de rango")


