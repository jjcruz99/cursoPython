import logging
from capa_datos_persona_POOL.conexion import Conexion
from capa_datos_persona_POOL.logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        logging.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb): #exc_tb = detalle de la Exepcion
        log.debug('Se ejecuta metodo __exit__')
        #Se verifica si ha ocurrido una exepcion
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrio una exepcion, se hace rollback : {exc_val} {exc_type} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug(('Commit de la transacción'))
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:## se llama indirectamente __init__ y __enter__ y cuando termina el with se llama __exit__
        log.debug('Dentro de with')
        cursor.execute('SELECT * FROM Persona')
        print(cursor.fetchall())



