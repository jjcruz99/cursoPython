from capa_datos_persona.conexion import Conexion
from capa_datos_persona.persona import Persona
from capa_datos_persona.logger_base import log

class PersonaDAO:
    '''
    DAO(Data Access Object)
    CRUD (Create-READ-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER by id_persona ASC'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_conexion() as conexion:
            with Conexion.obtener_cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                lista_persona = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    lista_persona.append(persona)

                return lista_persona

    @classmethod
    def insertar(cls,persona):
        with Conexion.obtener_conexion() :
            with Conexion.obtener_cursor() as cursor:
                print(f'Datos de la persona a insertar {persona}')
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Persona eliminada {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona eliminada {persona}')
                return cursor.rowcount

#pruebas locales
if __name__ == '__main__':
    #listar todos los datos de la entidad tabla
    lista_personas = PersonaDAO.seleccionar()
    for persona in lista_personas:
        print(persona.__str__())

    #insertar una persona a la BD
    # persona1 = Persona(nombre='esteban',apellido='Suarez',email='estebanano@email.com')
    # insertar_persona = PersonaDAO.insertar(persona1)
    # log.debug(insertar_persona)

    #actualizar persona
    # persona2 = Persona(id_persona=12,nombre='Esteban',apellido='Suarez',email='estebanano@email.com')
    # persona_actualizada = PersonaDAO.actualizar(persona2)
    # log.debug(persona_actualizada)

    #eliminar persona
    persona3 = Persona(id_persona=12)
    persona_eliminada = PersonaDAO.eliminar(persona3)
    log.debug(persona_eliminada)