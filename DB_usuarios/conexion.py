from logger_base import log
#pip install psycopg2
from psycopg2 import pool
import sys

class Conexion:
#atributos de clase protegidos
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        ##verificacion si el pool no eta creado
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion del pool exitosa. Deatlles :{cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al crear el pool. Destalles : {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexion obtenida del pool. :{conexion}')
        return conexion

    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresa la conexion al pool. : {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
        log.debug('Se cerraron todas las conexiones')

#pruebas locales
if __name__ == "__main__":
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    Conexion.cerrar_conexiones()
