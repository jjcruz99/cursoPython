
class Colegio:

    def __init__(self,clase,salon,cant_alumnos):
        # publico
        self.clase = clase
        # potegido
        self._salon = salon
        # privado
        self.__cant_alumnos = cant_alumnos



objecto1 = Colegio('Sociales',102,45)
print(objecto1.clase)
objecto1.clase = "Matematicas"
print(objecto1.clase)

#no es buena practica usar getters y setters 
print(objecto1._salon)

#no es buena practica
print(objecto1._Colegio__cant_alumnos)
objecto1._Colegio__cant_alumnos = 415
print(objecto1._Colegio__cant_alumnos)
