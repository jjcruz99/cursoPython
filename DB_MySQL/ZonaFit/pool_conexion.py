from mysql.connector import pooling
#from my
#Pool de conexiones es un grupo de objetos de conexion hacia la base de datos que van estar disposnibles

class Conexion:
    #atributos de clase
    #uso de mayusculas por que es una constante
    _DATABASE = 'zonafit_db'
    _USERNAME = 'root'
    _PASSWORD = 'admin'
    _DB_PORT = '3306'
    _HOST = 'localhost'
    _POOL_SIZe = 5
    _POOL_NAME = 'zonafit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool == None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls._POOL_NAME,
                    pool_size = cls._POOL_SIZe,
                    host= cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE,
                    user=cls._USERNAME,
                    password=cls._PASSWORD
                )
                print(f'Se creo el pool de conexiones: {cls.pool.pool_name}')
                return cls.pool
            except Exception as e:
                print(f'se presento un error al obtener el pool : {e}')
        else :
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return  cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()
        print(f'Se libero la conexion : {conexion}')

if __name__ == '__main__':
    # pool = Conexion.obtener_pool()
    # print(pool)
    #
    conexion1 = Conexion.obtener_conexion()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)