import psycopg2
# crear objeto conexion
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
##crear un cursor para ejecutar sentencias SQL
try:
    with conexion:
        with conexion.cursor() as cursor:
                sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
                #valores = (6,)
                entrada = input('Proporciona los id_persona a eliminar (Separados por una coma): ')
                valores = (tuple(entrada.split(',')),)
                cursor.execute(sentencia,valores)
                resgistros_eliminados = cursor.rowcount
                print(f'Registros eliminados: {resgistros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()