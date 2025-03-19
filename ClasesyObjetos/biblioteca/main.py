from ClasesyObjetos.biblioteca.biblioteca import Biblioteca

print('    Gestion de biblioteca')

#crear la biblioteca
biblioteca_ucc = Biblioteca('Sede Principal')

#agregar libros a la biblioteca
biblioteca_ucc.agregar_libros('La maria','Jorge Issac','Romantico')
biblioteca_ucc.agregar_libros('La hojarasca','Gabo','Suspenso')
biblioteca_ucc.agregar_libros('La odisea','Homero','Ficcion')

#mostrar todos los libros
biblioteca_ucc.mostrar_todos_libros()
biblioteca_ucc.buscar_libros_autor('Jorge Issac')
biblioteca_ucc.buscar_libros_genero('Suspenso')
biblioteca_ucc.buscar_libros_titulo('La odisea')
biblioteca_ucc.buscar_libros_titulo('Cien años de soledad')
