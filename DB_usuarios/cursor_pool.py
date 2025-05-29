from logger_base import log
from conexion import Conexion

class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    ## enter y exit permiten la creación de context managers que simplifican la gestión de recursos

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion= Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta metodo __exit__')
        if exc_val:
            self._conexion.rollback()##rollback no ejecuta la sentencia TSQL
            log.error(f''' Ocurrio un error, se ejecuta rollback
            valor: {exc_val}
            tipo: {exc_type}
            detalles: {exc_tb}''')
        else:
            self._conexion.commit()# commit guarda los cambios
            log.debug('Commit de la transaccion')
        self._cursor.close()#se debe cerrar el cursor
        Conexion.liberar_conexion(self._conexion) #devuelve la conexion al pool

#pruebas locales en la clase
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM usuarios')
        print(cursor.fetchall())