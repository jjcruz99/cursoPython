from capa_datos_persona_POOL.logger_base import log
class Persona:

    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
        id_persona = {self._id_persona}
        Nombre = {self._nombre}     
        Apellido = {self._apellido}
        Email = {self._email}
        '''

    #gettets y setters

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self,id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return  self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email = email

if __name__ == '__main__':
    persona1 = Persona(1,'John','Cruz','jj@email.com')
    log.debug(persona1)
    ##simular un insert
    persona2 = Persona(nombre='Shailo',apellido='Cruz',email='shailo@email.com')
    persona2.id_persona = 2 ##uso de setter para asignar el id 2
    log.debug(persona2)

    #simular delet
    persona2 = Persona(id_persona=2) #Elimina los demas atributos de la instancia

    print(persona2)
    #se elimino la instancia persona
    del persona2
    try:
        print(persona2)
    except Exception as e:
        print(f'Error al intentar acceder a la instancia persona2 : {e}')




