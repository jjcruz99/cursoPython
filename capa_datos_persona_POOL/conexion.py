
from logger_base import log
import psycopg2 as DB
from psycopg2 import pool
import sys
class Conexion:

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
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion del pool EXITOSA: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un Error al obtener el pool {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        ##Obtener objeto de conexiones
        conexion = cls.obtener_pool().getconn()
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresa la conexion al pool : {conexion}')

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
        log.debug('Se cerraron todas las conexiones')

#Pruebas locales
if __name__ == '__main__':
   conexion1 = Conexion.obtener_conexion()
   Conexion.liberar_conexion(conexion1)

   conexion2 = Conexion.obtener_conexion()

   #cerrar todas las conexiones
   Conexion.cerrar_conexiones()