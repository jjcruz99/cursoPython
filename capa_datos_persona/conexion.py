
from logger_base import log
import psycopg2 as DB
import sys
class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = DB.connect(
                    host = cls._HOST,
                    user= cls._USERNAME,
                    password = cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Conexxion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Error en la conexion : {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtener_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                log.debug('Se abrio correctamente el cursor')
                return cls._cursor
            except Exception as e:
                log.error(f'Se a presentado un error en el cursor {e}')
                sys.exit()
        else:
                log.debug('El cursor se ha generado correctamente')
                return cls._cursor


if __name__ == '__main__':
    Conexion.obtener_conexion()
    Conexion.obtener_cursor()